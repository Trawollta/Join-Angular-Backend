from rest_framework.permissions import IsAuthenticated
from .serializers import TaskCategorySerializer
from rest_framework import generics
from .models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class CreateTaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCategorySerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TaskListView(APIView):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = TaskCategorySerializer(tasks, many=True)
        return Response(serializer.data)

class DeleteTaskView(APIView):
    
    def delete(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return Response({"status": "success", "message": f"Task with id {task_id} deleted."})

class UpdateTaskView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCategorySerializer  
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
