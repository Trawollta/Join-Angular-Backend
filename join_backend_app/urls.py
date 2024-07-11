from django.contrib import admin
from django.urls import path, include
from authentication.views import RegisterView, CurrentUserView  # Verweis auf CurrentUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/auth/currentUser', CurrentUserView, basename='currentuser')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('contacts.urls')),
    path('', include(router.urls)),
    path('tasks/', include('tasks.urls')),
]
