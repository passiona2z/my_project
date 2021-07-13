from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import NewModel


def my_project(request):
    if request.method == "POST" :

        temp = request.POST.get('input_text')

        model_instance = NewModel()       # 저장하는 과정
        model_instance.text = temp
        model_instance.save()


        return render(request, 'accountapp/my_project.html',
                      context={'model_instance': model_instance})
    else :
        return render(request, 'accountapp/my_project.html',
                      context={'text': 'POST METHOD!'})
