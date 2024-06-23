from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at', 'project_lead', 'status', 'priority']
    list_filter = ['status', 'priority', 'created_at']
    search_fields = ['title', 'description']