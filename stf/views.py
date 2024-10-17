from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import UserRegisterForm


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