from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# class UserWins(models.Model):
#     userid = models.ForeignKey(User.id, verbose_name='username', on_delete=models.CASCADE)
#     user_wins = models.IntegerField(default=0)
#     def __str__(self):
#         return self.user

class Category(models.Model):
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Ip(models.Model): # наша таблица где будут айпи адреса
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class Task(models.Model):
    title = models.CharField(max_length=100)
    views = models.ManyToManyField(Ip, related_name="post_views", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    flag = models.CharField(max_length=150)
    describtion = models.CharField(max_length=1000)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
