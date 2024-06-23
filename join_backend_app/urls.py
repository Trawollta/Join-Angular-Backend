from django.contrib import admin
from django.urls import path, include
from authentication.views import UserListView, CurrentUserView  # Verweis auf CurrentUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),  # Authentifizierungs-URLs
    
    # Diese Pfade könnten auch über authentication.urls geleitet werden, um die Struktur zu vereinfachen
    path('api/auth/current_user/', CurrentUserView.as_view(), name='current_user'),
    path('api/auth/register/', UserListView.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('contacts.urls')),  
    path('tasks/', include('tasks.urls')),
]
