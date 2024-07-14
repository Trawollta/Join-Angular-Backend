from django.urls import path
from .views import RegisterView, LogoutView, LoginView, UserListView, UpdateUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('update-user/', UpdateUserView.as_view(), name='update-user'),
]
