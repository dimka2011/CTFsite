from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import UserWins, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("title", "describtion", "flag", "category", "reviews_qty")




    # title = serializers.CharField(max_length=100)
    # describtion = serializers.CharField(max_length=1000)
    # flag = serializers.CharField(max_length=100)
    # created_at = serializers.DateTimeField(read_only=True)
    # category_id = serializers.IntegerField()
    # reviews_qty = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Task.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.flag = validated_data.get("flag", instance.flag)
    #     instance.describtion = validated_data.get("describtion", instance.describtion)
    #     instance.save()
    #     return instance







# class TaskModel:
#     def __init__(self, title, flag, describtion):
#         self.title = title
#         self.flag = flag
#         self.describtion = describtion


# class UserSerializer(serializers.ModelSerializer):
#     title = serializers.CharField(max_length=100)
#     flag = serializers.CharField(max_length=255)
#     describtions = serializers.CharField(max_length=1000)
#
#
#
# class TaskSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     flag = serializers.CharField(max_length=255)
#     describtion = serializers.CharField(max_length=1000)
#
# def encode():
#     model = TaskModel("Your first CTF task", "You win!", "You")
#     model_sr = TaskSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

