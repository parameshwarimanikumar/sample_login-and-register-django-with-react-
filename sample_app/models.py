# sample_app/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Change the related_name to avoid clash
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Change the related_name to avoid clash
        blank=True,
    )

class GroupMessage(models.Model):
    # Your GroupMessage model fields here
    pass

class ChatGroup(models.Model):
    # Your ChatGroup model fields here
    pass
