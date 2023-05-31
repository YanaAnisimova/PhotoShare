import os

from django.db import IntegrityError
from django.contrib.auth.models import User

try:
    superuser = User.objects.create_superuser(
        username=os.getenv('DJANGO_SUPERUSER_NAME', default="admin"),
        email=os.getenv('DJANGO_SUPERUSER_EMAIL', default="admin@gmail.com"),
        password=os.getenv('DJANGO_SUPERUSER_PASSWORD', default="111"))
    superuser.save()
except IntegrityError:
    print(f"Super User with username {os.getenv('DJANGO_SUPERUSER_NAME')} is already exit!")
except Exception as e:
    print(e)
