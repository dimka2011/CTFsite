from django.urls import path
from . import views

app_name = 'CTF'
urlpatterns = [
    path("tasks/", views.TaskListCreate.as_view(), name="task-list"),
    path("category/", views.CategoryList.as_view(), name="category-list"),
    path("tasks/delete/<int:pk>/", views.TaskDelete.as_view(), name="delete-task"),
]