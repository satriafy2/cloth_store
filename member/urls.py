from django.urls import path

from . import views

urlpatterns = [
    # path('register', views.Users.as_view()),
    path('register', views.member_registration),
]
