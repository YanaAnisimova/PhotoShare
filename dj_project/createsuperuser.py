import os

from django.contrib.auth.models import Group
from django.db import IntegrityError

from group import Groups
from user_auth.models import User

try:
    superuser = User.objects.create_superuser(
        username=os.getenv('DJANGO_SUPERUSER_NAME', default="admin"),
        email=os.getenv('DJANGO_SUPERUSER_EMAIL', default="admin@gmail.com"),
        password=os.getenv('DJANGO_SUPERUSER_PASSWORD', default="111"),
        groups=Group.objects.get(
            name=os.getenv('DJANGO_SUPERUSER_GROUPS', default=Groups.ADMIN.value)
        )
    )
    superuser.save()
except IntegrityError:
    print(f"Super User with username {os.getenv('DJANGO_SUPERUSER_NAME')} is already exit!")
except Exception as e:
    print(e)
else:
    print(f"Super User with username {os.getenv('DJANGO_SUPERUSER_NAME')} created successfully.")
