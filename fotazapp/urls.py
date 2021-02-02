"""Fotazapp URLs module"""
from django.urls import path
from django.http import HttpResponse


def hello_world(request):
    """Return a greeting"""
    return HttpResponse('Hello, world!')

urlpatterns = [
    path('hello-world/', hello_world)
]
