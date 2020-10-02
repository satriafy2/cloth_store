from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods as req_methods
from django.views import View

from .models import Member, Transaction
from admin.models import Item
from project_bajigur.utils import exec_query

from dateutil.relativedelta import relativedelta
import random
import datetime
import json

@req_methods(['POST'])
def member_registration(request):
    try:
        data = json.loads(request.body)
        if not {'email', 'name', 'sex', 'birth_date'} <= set(data):
            return JsonResponse({"status": "error"}, status=400)

        m = Member(
            email=data['email'],
            name=data['name'],
            sex=data['sex'],
            birth_date=data['birth_date'])
        m.save()

        return JsonResponse({"status": "ok"}, status=200)

    except Exception as e:
        print(e)
        return JsonResponse({"status": "unknown error"}, status=500)


@req_methods(['POST'])
def member_buy_items(request):
    try:
        data = json.loads(request.body)
        if not {'items', 'id_member'} <= set(data):
            return JsonResponse({"status": "error"}, status=400)

        if not _validate_member(data['id_member']):
            return JsonResponse({"status": "invalid member"}, status=400)

        objs = []
        for v in data['items']:
            price = _get_item_price(v['id_item'])
            if price < 0:
                return JsonResponse({"status": "invalid id item"}, status=400)

            price_total = v['qty'] * price
            objs.append(
                Transaction(
                    id_member=data['id_member'],
                    id_item=v['id_item'],
                    qty=v['qty'],
                    total=price_total
            ))

        Transaction.objects.bulk_create(objs)
        return JsonResponse({"status": "ok"}, status=200)

    except Exception as e:
        print(e)
        return JsonResponse({"status": "unknown error"}, status=500)


@req_methods(['GET'])
def member_get_trending(request):
    # period = 'week'/'month'
    try:
        period = request.GET.get('period', 'week')
        if period not in ['week', 'month']:
            return JsonResponse({"status": "invalid period"}, status=400)

        today = datetime.date.today()
        if period == 'week':
            start_date = today - relativedelta(days=7)

        elif period == 'month':
            start_date = today - relativedelta(months=1)

        sql = "SELECT * FROM ( \
            SELECT bt.id_item, bi.NAME, SUM( bt.qty ) AS count \
            FROM bajigur_transaction bt \
            LEFT JOIN bajigur_items bi ON bi.id_item = bt.id_item \
            WHERE trx_date >= %s \
            GROUP BY id_item \
        ) AS tabel ORDER BY count DESC LIMIT 10 "
        res = exec_query(sql, [start_date], 1)

        return JsonResponse({"status": "ok", "data": res}, status=200)

    except Exception as e:
        print(e)
        return JsonResponse({"status": "unknown error"}, status=500)


@req_methods(['POST'])
def member_get_recommended(request):
    try:
        data = json.loads(request.body)
        if not {'id_member'} <= set(data):
            return JsonResponse({"status": "error"}, status=400)

        if not _validate_member(data['id_member']):
            return JsonResponse({"status": "invalid member"}, status=400)

        # get 2 latest transaction
        obj = Transaction.objects.filter(
            id_member=data['id_member']).order_by('-trx_date')[:2]

        category = []
        for val in obj.values():
            res = _get_item_category(val['id_item'])
            res = json.loads(res['category'])
            category.extend(res)

        category        = list(set(category))
        recomm_items    = []

        for _ in range(5):
            sql = "SELECT id_item FROM bajigur_items \
                WHERE "

            # ambil 2 random category
            # agar mendapatkan item dengan 1/2 kategori yang sama
            rand_cat = [
                random.choice(category),
                random.choice(category)
            ]

            temp, params = [], []
            for v in rand_cat:
                temp.append("category LIKE %s")
                params.append(f"%{v}%")

            sql+= " AND ".join(temp)
            sql+= " ORDER BY rand() LIMIT 1 "

            res = exec_query(sql, params, 1)
            if len(res) > 0:
                recomm_items.append(res[0]['id_item'])

        recomm_items = list(set(recomm_items))

        sql = "SELECT * FROM bajigur_items WHERE id_item IN ({}) ".format(
            ', '.join(['%s' for _ in recomm_items]))
        res = exec_query(sql, recomm_items, 1)

        for v in res:
            v['category'] = json.loads(v['category'])

        return JsonResponse({"status": "ok", "data": res}, status=200)

    except Exception as e:
        print(e)
        return JsonResponse({"status": "unknown error"}, status=500)


def _validate_member(id):
    res = list(Member.objects.filter(id_member=id).values())
    return True if len(res) > 0 else False


def _get_item_price(id):
    res = list(Item.objects.filter(id_item=id).values())
    if len(res) < 1:
        return -1

    else:
        return res[0]['price']


def _get_item_category(id):
    res = Item.objects.filter(id_item=id).values('category')
    return res[0]
