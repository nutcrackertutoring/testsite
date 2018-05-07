from django.db import models

from django_use_email_as_username.models import BaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager




class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: email})

class CustomUser(BaseUser):
    objects = CustomUserManager()