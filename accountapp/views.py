from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def my_project(request):
    return HttpResponse("Hello, this is my project")
