from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    color = serializers.CharField(source='profile.color', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'color'] 

class TaskCategorySerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    color = serializers.CharField(source='profile.color', read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
        extra_kwargs = {'created_by': {'read_only': True}}

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['assigned_to'] = UserSerializer(instance.assigned_to.all(), many=True).data
        return ret
