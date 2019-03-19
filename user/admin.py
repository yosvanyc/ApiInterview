from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'password')


admin.site.register(User, CustomUserAdmin)


