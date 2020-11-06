from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('create_user', views.create),
    path('create_user_ajax', views.create_ajax),
]