# Generated by Django 5.0.6 on 2024-07-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_task_category_task_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='color',
        ),
        migrations.AddField(
            model_name='task',
            name='subtasks',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
