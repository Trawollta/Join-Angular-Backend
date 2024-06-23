from rest_framework import serializers
from .models import Task


class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        extra_kwargs = {'created_by': {'read_only': True}}



