from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import UserRegistrationSerializer, LoginSerializer
from django.contrib.auth import get_user_model


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]  # Keine Authentifizierung erforderlich

class CustomObtainAuthToken(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class LoginView(ObtainAuthToken):

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            userData = serializer.validated_data
            if userData['username']:
                try:
                    user = get_user_model().objects.get(username=userData['username'])
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({'token': token.key, 'user_id': user.pk, 'username': user.username})
                except user.DoesNotExist:
                    return Response('User not found', status=status.HTTP_404_NOT_FOUND)
            else:
                return Response('username field is required', status=status.HTTP_400_BAD_REQUEST)

        else:
            userData = serializer.data
            if serializer.data.get('username'):
                try:
                    user = get_user_model().objects.get(username=userData['username'])
                    if not user.is_active:
                        return Response('username not activated!',status=status.HTTP_403_FORBIDDEN)
                    else:
                        return Response('Wrong username or password',status=status.HTTP_401_UNAUTHORIZED)
                except get_user_model().DoesNotExist:
                    return Response('User not found', status=status.HTTP_404_NOT_FOUND)
            else:
                return Response('username field is required', status=status.HTTP_400_BAD_REQUEST)

    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Token.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user= get_object_or_404(User, pk=request.id)
        
        return Response({
            'username': user.username,
            'first_name':user.first_name,
            'last_name': user.last_name,
            
            
            
        })

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]
