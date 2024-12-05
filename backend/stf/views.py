from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.db import transaction
from django.db.models import F
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, FileResponse
from pytils.translit import slugify
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTStatelessUserAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from . import models
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import UserRegisterForm, FlagForm, ProfileForm, UserForm
from rest_framework import generics, viewsets
import asyncio
from .forms import TaskForm
from .serializers import TaskSerializer, UserSerializer, CategorySerializer
from django import forms
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    authentication_classes = ()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    authentication_classes = [JWTAuthentication, JWTStatelessUserAuthentication]
    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = User.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj


class TaskListCreate(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()

class TaskDelete(generics.DestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user)


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


def index(request):
    tasks = Task.objects.all()

    new_solved_tasks = []
    try:
        new_solved_task = str(Profile.objects.get(user=request.user).solved_tasks)
        for new in new_solved_task.split(' '):
            try:
                new_solved_tasks.append(int(new))
            except ValueError:
                pass
    except TypeError:
        new_solved_tasks = []
    print(new_solved_tasks)
    return render(request, 'tasks.html', {
        'tasks': tasks,
        'solved_tasks': new_solved_tasks
    })


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip


def single_task(request, task_id):
        try:
            task = Task.objects.get(pk=task_id)
            ip = get_client_ip(request)
            if Ip.objects.filter(ip=ip).exists():
                task.views.add(Ip.objects.get(ip=ip))
            else:
                Ip.objects.create(ip=ip)
                task.views.add(Ip.objects.get(ip=ip))

            try:
                new_solved_task = str(Profile.objects.get(user=request.user).solved_tasks)
                context = {
                    'task': task,
                    'task_id': str(task_id),
                    'form': FlagForm,
                    'solved_tasks': new_solved_task.split(' '),
                    'views': task.views.count()
                }
                return render(request, 'single_task.html', context)

            except:
                context = {
                    'task': task,
                    'task_id': str(task_id),
                    'form': FlagForm,
                    'views': task.views.count()
                }
                return render(request, 'done_task.html', context)

        except Task.DoesNotExist:
            raise Http404()


def task_file(request, task_id):
    try:
        model = Task.objects.get(id=task_id)
        return FileResponse(model.file, as_attachment=True)
    except:
        return render(request, 'no_file.html')

def flagform(request, task_id):
    if request.method == 'GET':
        TaskObj = Task.objects.get(id=task_id)
        ProfileOb = Profile.objects.filter(user_id=request.user.id)
        print(request.GET.get('user_flag'))
        print(TaskObj.flag)
        SolvedTask = str(Profile.objects.get(user=request.user).solved_tasks)
        if str(task_id) not in SolvedTask.split():
            if TaskObj.flag == request.GET.get('user_flag'):
                new_solved_task = Profile.objects.get(user=request.user).solved_tasks + ' ' + str(task_id)
                print(new_solved_task)
                ProfileOb.update(user_wins=F("user_wins") + 1)
                ProfileOb.update(solved_tasks=new_solved_task)
                return render(request, 'good_flag.html')
            else:
                return render(request, 'bad_flag.html')
        else:
            task = Task.objects.get(pk=task_id)
            return render(request, 'done_task.html', {'task': task})


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_tasks': Task.objects.filter(author=request.user.id)
    })



def get_username(id):
    user = User.objects.get(id=id)
    print(user)
    return user.username

def winners(request):
    winners = Profile.objects.filter().order_by('-user_wins')
    win_list = []
    for winner in winners:
        win = str(winner.user) + '-' + str(winner.user_wins) + ' wins'
        print(win)
        win_list.append(win)
    context = {'winners': winners.values('user', 'user_wins'),
               'get_username()': get_username,
               'list': win_list}
    return render(request, 'winners.html', context)

def user_in_autor(user):
    groups = user.groups.all()
    print('Автор' in [group.name for group in groups])
    return 'Автор' in [group.name for group in groups]
class NewTask(UserPassesTestMixin, CreateView):
    template_name = 'new_task.html'
    form_class = TaskForm
    model = Task

    def test_func(self):
        return self.request.user.groups.filter(name='Автор').exists()

    def get_success_url(self):
        return reverse('profile')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        form.instance.author = self.request.user
        return super().form_valid(form)

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    print(Task.objects.get(id=task_id).author)
    if request.user == task.author:
        task.delete()
        return render(request, 'delete_task.html')
    elif request.user != task.author:
        raise PermissionDenied()