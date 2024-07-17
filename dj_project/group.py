import os
from enum import Enum

import django
from django.contrib.auth.models import Group

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_project.settings')
django.setup()


class Groups(Enum):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    SIMPLE_USER = 'simple_user'


for group in Groups:
    new_group, created = Group.objects.get_or_create(name=group.value)
