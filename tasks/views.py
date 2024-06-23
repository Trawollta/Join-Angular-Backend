from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import TaskCategorySerializer
from rest_framework import generics
from .models import Task
from rest_framework.views import APIView
from .serializers import TaskCategorySerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class CreateTaskView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskCategorySerializer 
    # queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class TaskListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = TaskCategorySerializer(tasks, many=True)
        return Response(serializer.data)
    
class DeleteTaskView(generics.GenericAPIView):
    serializer_class = TaskCategorySerializer

    def delete(self, request, *args, **kwargs):
        task_id = request.query_params.get('task_id')
        if not task_id:
            return Response({"error": "Task ID is required"}, status=400)
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return Response({"status": "success", "message": f"Task with id {task_id} deleted."})

class UpdateTaskView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCategorySerializer
    lookup_field = 'id'
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
