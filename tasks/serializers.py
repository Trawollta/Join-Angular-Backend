from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name', 'last_name']


class TaskCategorySerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    assigned_to = UserSerializer(many=True)
    class Meta:
        model = Task
        fields = "__all__"
        extra_kwargs = {'created_by': {'read_only': True}}



