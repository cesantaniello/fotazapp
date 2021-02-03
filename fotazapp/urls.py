"""Fotazapp URLs module"""
from django.urls import path

from fotazapp import views


urlpatterns = [
    path('hello-world/', views.hello_world),
    path('sorted/', views.sorted_integers),
    path('hi/<str:name>/<int:age>', views.say_hi),
]
