from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import Profile

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    color = serializers.CharField(write_only=True) 

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'color']

    def create(self, validated_data):
        color = validated_data.pop('color')
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(**validated_data, password=password)
        profile, created = Profile.objects.get_or_create(user=user)
        profile.color = color
        profile.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = ('username','password')
        read_only_fields = ('username', )

    def validate(self, data):
        user = authenticate_with_username_and_password(data["username"], data["password"])
        if user:
            if user.is_active:
                return {'username': user.username, 'password': user.password}
        raise serializers.ValidationError("Incorrect Credentials")
    
def authenticate_with_username_and_password(username, password):
    user = get_user_model()
    try:
        user = user.objects.get(username=username)
        if user.check_password(password):
            return user
    except user.DoesNotExist:
        return None
    
    
class UserSerializer(serializers.ModelSerializer):
    color = serializers.CharField(source='profile.color', required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'color']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        color = profile_data.get('color')

        instance = super().update(instance, validated_data)

        # Update profile instance
        profile = instance.profile
        if color:
            profile.color = color
        profile.save()

        return instance