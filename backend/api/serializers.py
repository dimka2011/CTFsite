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
class TaskCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "flag"]

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "bio", "location", "birth_date"]
        
    def update(self, instance, validated_data):
        instance.bio = validated_data.get("bio", instance.bio)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.location = validated_data.get("location", instance.location)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ("__all__")

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "content", "created_at", "author", "flag"]
        extra_kwargs = {"author": {"read_only": True}}

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "content", "category", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title"]