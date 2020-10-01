from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods as req_methods
from django.views import View

from .models import Member
import json

@req_methods(['POST'])
def member_registration(request):
    try:
        data = json.loads(request.body)
        if not {'email', 'name', 'sex', 'birth_date'} <= set(data):
            return JsonResponse({"status": "error"}, status=400)

        m = Member(
            email=data['email'], name=data['name'], sex=data['sex'],
            birth_date=data['birth_date'])
        m.save()

        return JsonResponse({"status": "success"}, status=200)

    except Exception as e:
        print(e)
        return JsonResponse({"status": "unknown error"}, status=500)

# class Users(View):
#     def post(self, request):
#         print(request.body)
#         return JsonResponse({
#             'data': 'oke'
#         })
#
#     def delete(self, request):
#         return JsonResponse({"hapus": 20})
