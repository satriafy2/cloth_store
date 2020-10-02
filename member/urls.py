from django.urls import path

from . import views

urlpatterns = [
    path('register', views.member_registration),
    path('buy_items', views.member_buy_items),
    path('trending', views.member_get_trending),
    path('recommended', views.member_get_recommended)
]
