from authentication.models import Profile
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Contact

class ContactListSerializer(serializers.ModelSerializer):
    color = serializers.CharField(source='profile.color', read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'id', 'color']

class ContactCreateSerializer(serializers.ModelSerializer):
    color = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'color']

    def create(self, validated_data):
        color = validated_data.pop('color')
        email = validated_data['email']
        username = self.generate_unique_username(email)
        user = User.objects.create(username=username, **validated_data)
        user.set_password(User.objects.make_random_password())
        user.save()
        profile=Profile.objects.create(user=user, color=color)
        profile.color= color
        profile.save()
        return user

    def generate_unique_username(self, email):
        base_username = email.split('@')[0]
        username = base_username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1
        return username

class ContactUpdateSerializer(serializers.ModelSerializer):
    color = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'color']

    def update(self, instance, validated_data):
        color = validated_data.pop('color', None)
        user = super().update(instance, validated_data)
        if color is not None:
            profile = Profile.objects.get(user=user)
            profile.color = color
            profile.save()
            return user


class ContactDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id']
