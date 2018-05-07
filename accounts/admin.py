from django.contrib import admin
from django_use_email_as_username.admin import BaseUserAdmin

from .models import CustomUser

admin.site.register(CustomUser, BaseUserAdmin)

# Register your models here.
