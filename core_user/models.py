from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    settings = models.JSONField(default=dict, null=True, blank=True)
    status = models.PositiveIntegerField(null=True, blank=True)

