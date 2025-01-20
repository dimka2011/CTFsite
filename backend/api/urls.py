from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.TaskList.as_view(), name="task-list"),
    path("tasks/create/", views.TaskCreate.as_view(), name="task-create"),
    path("tasks/delete/<int:pk>/", views.TaskDelete.as_view(), name="delete-task"),
    path("category/", views.CategoryList.as_view(), name="category-list"),    
    path("tasks/<int:pk>/", views.OneTask.as_view(), name="task-list"),
    path("tasks/check/", views.CheckFlag.as_view(), name="check")
]