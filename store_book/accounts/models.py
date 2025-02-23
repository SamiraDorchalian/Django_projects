from django.db import models
from django.contrib.auth.models import AbstractUser

# auth app -> models.User
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
