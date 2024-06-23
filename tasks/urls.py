from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateTaskView, TaskListView, DeleteTaskView, UpdateTaskView



urlpatterns = [
    path('createTask/', CreateTaskView.as_view(), name='createTasks'),
    path('getTasks/', TaskListView.as_view(), name='TaskList'),
    path('deleteTask/', DeleteTaskView.as_view(), name='delete_task'),
    path('updateTask/<str:id>/', UpdateTaskView.as_view(), name='update_task'),
]