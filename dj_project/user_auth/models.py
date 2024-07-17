from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)  # reset on_delete=models.PROTECT
    email = models.EmailField(max_length=50, unique=True)

    REQUIRED_FIELDS = ['groups_id', 'email']

    def __str__(self):
        return self.username
