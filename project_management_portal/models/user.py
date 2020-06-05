from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name  = models.CharField(max_length=100)
    profile_pic = models.CharField(max_length=50, default="")
    is_admin = models.BooleanField(default=False)
