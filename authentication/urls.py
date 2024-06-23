from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CurrentUserView, RegisterView, LogoutView, CustomTokenObtainPairView

urlpatterns = [
    path('current_user/', CurrentUserView.as_view(), name='current_user'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
