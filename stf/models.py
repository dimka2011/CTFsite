from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    flag = models.CharField(max_length=150)
    describtion = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
