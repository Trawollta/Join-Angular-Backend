# Generated by Django 5.0.6 on 2024-07-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='extra_field',
        ),
        migrations.AddField(
            model_name='profile',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]