from django.http import JsonResponse
from django.views import View

from .models import Item, OnSale
import json
import datetime


class Items(View):
    def get(self, request):
        try:
            id = request.GET.get('id', None)
            if id is None:
                res = list(Item.objects.values())

            else:
                res = list(Item.objects.filter(id_item=id).values())

            return JsonResponse({'status':'ok', 'data': res}, status=200)

        except Exception as e:
            print(e)
            return JsonResponse({"status": "unknown error"}, status=500)


    def post(self, request):
        try:
            data = json.loads(request.body)
            if not {'name', 'size', 'price', 'category'} <= set(data):
                return JsonResponse({"status": "error"}, status=400)

            m = Item(
                name=data['name'],
                size=data['size'],
                price=data['price'],
                category=json.dumps(data['category']))
            m.save()

            return JsonResponse({"status": "success"}, status=200)

        except Exception as e:
            print(e)
            return JsonResponse({"status": "unknown error"}, status=500)


    def delete(self, request):
        try:
            data = json.loads(request.body)
            if not {'id'} <= set(data):
                return JsonResponse({"status": "error"}, status=400)

            Item.objects.filter(id_item=data['id']).delete()
            return JsonResponse({"status": "ok"}, status=200)

        except Exception as e:
            print(e)
            return JsonResponse({"status": "unknown error"}, status=500)


class Onsales(View):
    def get(self, request):
        try:
            id = request.GET.get('id', None)
            if id is None:
                res = list(OnSale.objects.values())

            else:
                res = list(OnSale.objects.filter(id_sale=id).values())

            return JsonResponse({'status':'ok', 'data': res}, status=200)

        except Exception as e:
            print(e)
            return JsonResponse({"status": "unknown error"}, status=500)


    def post(self, request):
        try:
            data = json.loads(request.body)
            if not {'id_item', 'discount', 'sale_start', 'sale_expiry'} <= set(data):
                return JsonResponse({"status": "error"}, status=400)

            if not _validate_item(data['id_item']):
                return JsonResponse({"status": "invalid id item"}, status=400)

            if data['discount'] > 99:
                return JsonResponse({"status": "invalid discount"}, status=400)

            m = OnSale(
                id_item=data['id_item'],
                discount=data['discount'],
                sale_start=data['sale_start'],
                sale_expiry=data['sale_expiry'])
            m.save()

            return JsonResponse({"status": "success"}, status=200)

        except Exception as e:
            print(e)
            return JsonResponse({"status": "unknown error"}, status=500)


    def delete(self, request):
        try:
            data = json.loads(request.body)
            if not {'id'} <= set(data):
                return JsonResponse({"status": "error"}, status=400)

            OnSale.objects.filter(id_sale=data['id']).delete()
            return JsonResponse({"status": "ok"}, status=200)

        except Exception as e:
            print(e)
            return JsonResponse({"status": "unknown error"}, status=500)


def _validate_item(id):
    res = list(Item.objects.filter(id_item=id).values())
    if len(res) < 1:
        return False

    return True
