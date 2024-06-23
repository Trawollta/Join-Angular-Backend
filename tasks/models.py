from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.conf import settings


PRIORITY_CHOICES = (
     ("Low", "Low"),
    ("Medium", "Medium"),
    ("Urgent", "Urgent"),
)

STATUS_CHOICES = (
    ("TO_DO", "TO_DO"),
    ("AWAIT_FEEDBACK", "AWAIT_FEEDBACK"),
    ("IN_PROGRESS", "IN_PROGRESS"),
    ("DONE", "DONE")
)

class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=600)
    project_lead = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="project_leads",
    null=True,  # Erlaubt NULL-Werte in der Datenbank
    blank=True  # Erlaubt das Feld leer zu lassen im Admin und in Formularen
)
    created_at = models.DateField(("Created"), auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="TO_DO")
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES, default="Low")
    created_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_tasks"
)


    def __str__(self):
        return self.title
