from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]  # Keine Authentifizierung erforderlich

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.headers)
        serializer = UserRegistrationSerializer(request.user)
        return Response(serializer.data)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            print("Erhaltener Refresh-Token:", refresh_token)
            if refresh_token:
                token = RefreshToken(refresh_token)
                print("Token erfolgreich erstellt:", token)
                token.blacklist()
                return Response(status=status.HTTP_205_RESET_CONTENT)
            else:
                print("Kein Refresh-Token erhalten")
                return Response({"detail": "Refresh-Token wird benötigt"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("Fehler beim Abmelden:", str(e))
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

