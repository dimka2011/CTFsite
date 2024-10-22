from django.urls import path
from . import views

app_name = 'CTF'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.single_task, name='single_task'),
    path('newtask/', views.NewTask.as_view(), name='new_task'),
    path("signup/", views.UserRegisterView.as_view(), name='signup'),
    path('<int:task_id>/flag/', views.flagform, name='flag'),
    path('winners/', views.winners, name='winners')
    ]