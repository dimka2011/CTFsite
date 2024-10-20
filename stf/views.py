from django.contrib.auth.models import User
from django.db.models import F
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from . import models
from .models import Task, Category, Ip
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import UserRegisterForm, FlagForm
from rest_framework import generics, viewsets
import asyncio
from .serializers import TaskSerializer
from django import forms
from django.contrib import auth


# class UsersViewSet(viewsets.ModelViewSet):
#     queryset = UserWins.objects.all()
#     serializer_class = UserSerializer


# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.title})

class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TaskAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class TaskAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAdminOrReadOnly,)


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


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip


def single_task(request, task_id):
    try:
        task = models.Task.objects.get(pk=task_id)
        ip = get_client_ip(request)
        if Ip.objects.filter(ip=ip).exists():
            task.views.add(Ip.objects.get(ip=ip))
        else:
            Ip.objects.create(ip=ip)
            task.views.add(Ip.objects.get(ip=ip))

        context = {
            'task': task,
            'form': FlagForm,
        }
        return render(request, 'single_task.html', context)
    except models.Task.DoesNotExist:
        raise Http404()


def flagform(request, task_id):
    if request.method == 'GET':
        TaskObj = Task.objects.get(id=task_id)
        print(request.GET.get('user_flag'))
        print(TaskObj)
        if TaskObj.flag == request.GET.get('user_flag'):
            user = User.objects.filter(id=request.user.id).update(user_wins = F("user_wins") + 1)
            return render(request, 'good_flag.html')
        else:
            return render(request, 'bad_flag.html')
