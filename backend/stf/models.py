from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    solved_tasks = models.CharField(max_length=10000000, default='0')
    user_wins = models.IntegerField(default=0)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Category(models.Model):
    title = models.CharField(max_length=300)
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
    file = models.FileField(upload_to="files/", null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")


    def __str__(self):
        return self.title
