from django.contrib.auth.models import User
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .models import Profile
from tasks.serializers import UserSerializer
from .serializers import UserRegistrationSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import get_user_model

class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)

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
                    return Response('Benutzer nicht gefunden', status=status.HTTP_404_NOT_FOUND)
            else:
                return Response('Das Feld "Benutzername" ist erforderlich', status=status.HTTP_400_BAD_REQUEST)

        else:
            userData = serializer.data
            if serializer.data.get('username'):
                try:
                    user = get_user_model().objects.get(username=userData['username'])
                    if not user.is_active:
                        return Response('Benutzername nicht aktiviert!',status=status.HTTP_403_FORBIDDEN)
                    else:
                        return Response('Falscher Benutzername oder Passwort',status=status.HTTP_401_UNAUTHORIZED)
                except get_user_model().DoesNotExist:
                    return Response('Benutzer nicht gefunden', status=status.HTTP_404_NOT_FOUND)
            else:
                return Response('Das Feld "Benutzername" ist erforderlich', status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Token.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CurrentUserView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        # This now correctly returns a queryset of the User model filtered to the current user
        return get_user_model().objects.filter(id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)  # This correctly

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]
