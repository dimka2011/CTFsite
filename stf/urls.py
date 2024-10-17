from django.urls import path
from . import views

app_name = 'CTF'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>', views.single_task, name='single_task'),
    path("signup/", views.UserRegisterView.as_view(), name='signup')
    ]