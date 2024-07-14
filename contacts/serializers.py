from rest_framework import serializers
from django.contrib.auth.models import User

class ContactListSerializer(serializers.ModelSerializer):
    color = serializers.CharField(source='profile.color', read_only=True) 
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'id', 'color']
