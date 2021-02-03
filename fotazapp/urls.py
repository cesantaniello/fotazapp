"""Fotazapp URLs module"""
from django.urls import path

from fotazapp import views


urlpatterns = [
    path('hello-world/', views.hello_world),
    path('hi/', views.hi),
]
