# Generated by Django 5.0.6 on 2024-07-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_remove_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]