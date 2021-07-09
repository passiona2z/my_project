from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def my_project(request):
    if request.method == "POST" :
        return render(request, 'accountapp/my_project.html',
                      context={'text': 'POST METHOD!'})
    else :
        return render(request, 'accountapp/my_project.html',
                      context={'text': 'POST METHOD!'})
