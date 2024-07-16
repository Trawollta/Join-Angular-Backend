# Generated by Django 5.0.6 on 2024-07-16 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(default='Allgemein', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]