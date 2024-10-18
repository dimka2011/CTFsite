from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from .models import UserWins, Task
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import UserRegisterForm
from rest_framework import generics

from .serializers import TaskSerializer


class UsersAPIView(APIView):
    def get(self, request):
        return Response({'title': 'Your first task'})


class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAPIUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# class TaskAPIView(APIView):
#
#     def get(self, request):
#         t = Task.objects.all().values()
#         return Response({'tasks': TaskSerializer(t, many=True).data})
#     def post(self, request):
#         serializer = TaskSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # post_new = Task.objects.create(
#         #     title=request.data['title'],
#         #     flag=request.data['flag'],
#         #     describtion=request.data['title'],
#         #     reviews_qty=request.data['reviews_qty'],
#         #     category_id=request.data['category_id'],
#         # )
#
#         return Response({'post': serializer.data})
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Task.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#         serializer = TaskSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})


class UserRegisterView(CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context


class ProfilePage(TemplateView):
    template_name = "registration/profile.html"

'''class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"'''

def index(request):
    tasks = models.Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

def single_task(request, task_id):
    try:
        task = models.Task.objects.get(pk=task_id)
        return render(request, 'single_task.html', {'task': task})
    except models.Task.DoesNotExist:
        raise Http404()