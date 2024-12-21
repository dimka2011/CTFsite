from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, Category
from users.models import User
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name", "email", "bio", "win_list", "location", "birth_date", "date_joined"]
        extra_kwargs = {"password": {"write_only": True}}
    
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "bio", "location", "birth_date"]
        
    def update(self, instance, validated_data):
        instance.bio = validated_data.get("bio", instance.bio)
        instance.save()
        return instance
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ("__all__")

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "content", "flag", "category", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title"]