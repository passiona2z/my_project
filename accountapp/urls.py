from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accountapp.views import my_project, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('my_project/', my_project, name='my_project'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create')

]