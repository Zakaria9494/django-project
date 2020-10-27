from django.urls import path
from .import views
from rest_framework import routers
from django.conf.urls import include


urlpatterns = [
    path('first', views.first),
 
]
