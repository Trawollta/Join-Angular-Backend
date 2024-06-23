# from django.db import models

# class Contact(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15, blank=True)

#     def __str__(self):
#         return self.name


from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contact', null=True)
    additional_info = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'No User'}"
