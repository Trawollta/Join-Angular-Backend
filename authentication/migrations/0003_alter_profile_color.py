# Generated by Django 5.0.6 on 2024-07-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_profile_extra_field_profile_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
