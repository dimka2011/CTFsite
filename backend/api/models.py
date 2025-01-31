from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _

from django.conf import settings


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     solved_tasks = models.CharField(max_length=10000000, default='0')
#     user_wins = models.IntegerField(default=0)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return self.user.username



    
# class User(AbstractBaseUser, PermissionsMixin):
#     user = models.CharField(_("username"), unique=True)
#     email = models.EmailField(_('email'), unique=True)
#     first_name = models.CharField(_('name'), max_length=30, blank=True)
#     last_name = models.CharField(_('surname'), max_length=30, blank=True)
#     date_joined = models.DateTimeField(_('registered'), auto_now_add=True)
#     bio = models.TextField(_('bio'), max_length=1000, blank=True)
#     win_list = models.TextField(_("win_list"), default="0")
#     is_active = models.BooleanField(_('is_active'), default=True)

#     objects = BaseUserManager()

#     USERNAME_FIELD = 'user'
#     REQUIRED_FIELDS = []

    # class Meta:
    #     verbose_name = _('user')
    #     verbose_name_plural = _('users')
    # def get_full_name(self):
    #     '''
    #     Возвращает first_name и last_name с пробелом между ними.
    #     '''
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()

    # def get_short_name(self):
    #     '''
    #     Возвращает сокращенное имя пользователя.
    #     '''
    #     return self.first_name
    
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Category(models.Model):
    title = models.CharField(max_length=300)
    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    flag = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title