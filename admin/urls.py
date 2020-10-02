from django.urls import path

from . import views

urlpatterns = [
    path('item', views.Items.as_view()),
    path('onsale', views.Onsales.as_view()),
    # path('item', views.member_registration),
]
