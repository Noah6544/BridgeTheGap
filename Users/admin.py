# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['Username']}),
        ('User Information', {'fields': ['first_name']})

    ]

