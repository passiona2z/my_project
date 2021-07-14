from django.urls import path

from accountapp.views import my_project, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('my_project/', my_project, name='my_project'),

    path('create/', AccountCreateView.as_view(), name='create')

]