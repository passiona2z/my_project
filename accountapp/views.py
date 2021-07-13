

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import NewModel


def my_project(request):
    if request.method == "POST" :

        temp = request.POST.get('input_text')

        model_instance = NewModel()       # 저장하는 과정
        model_instance.text = temp
        model_instance.save()

        return HttpResponseRedirect(reverse('accountapp:my_project'))

    else :
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/my_project.html',
                      context={'data_list': data_list})
