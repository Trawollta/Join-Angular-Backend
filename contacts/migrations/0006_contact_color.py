# Generated by Django 5.0.6 on 2024-07-17 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_remove_contact_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='color',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
