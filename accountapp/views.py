from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def my_project(request):
    return render(request, 'accountapp/my_project.html')
