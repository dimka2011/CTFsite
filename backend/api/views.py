from django.shortcuts import render, HttpResponse
from users import models
from rest_framework import generics 
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny # type: ignore
from .models import Task, Category


class TaskList(generics.ListAPIView):
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.all()


class TaskCreate(generics.CreateAPIView):
    serializer_class = TaskCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Category.objects.all()

class TaskDelete(generics.DestroyAPIView):
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user)

class UserView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = models.User.objects.filter(id=self.request.user.id)
        return user

class UpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = models.User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

class CreateUserView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class OneTask(generics.ListAPIView):
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.build_absolute_uri().strip("/").split("/")[-1])
        return Task.objects.filter(pk=self.request.build_absolute_uri().strip("/").split("/")[-1])

def appendWins(user, task_id):
    user.win_list = str(user.win_list) + "," + str(task_id)
    user.save()
    print(user.win_list)


class CheckFlag(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]   
    def get(self, request):
        task_id = request.GET.get('task_id')
        user_flag = request.GET.get('flag')
        user = request.user
        user_wins = user.win_list.split(",")
        if task_id not in user_wins:
            try:
                task_flag = Task.objects.get(id=task_id)
                print(task_id, user_flag, task_flag.flag)
                if user_flag==task_flag.flag:
                    appendWins(user, task_id)
                    return HttpResponse("Good", content_type='application/json')
                else:
                    return HttpResponse("Bad", content_type='application/json')
            except ValueError:
                return HttpResponse("Not found", content_type='application/json')
        else:
            return HttpResponse("Done", content_type='application/json')