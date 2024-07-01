from django.urls import path
from .views import CurrentUserView, RegisterView, LogoutView, CustomObtainAuthToken, UserListView

urlpatterns = [
    path('current_user/', CurrentUserView.as_view(), name='current_user'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UserListView.as_view(), name='user_list'),
]
