from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

class CustomUserAdmin(UserAdmin):
    search_fields = ( 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_admin', 'is_superuser', 'is_admin', 'is_staff')
    ordering = ('email',)


    fieldsets = (
        (None, {
            "fields": (
                'email',
                'first_name',
                'last_name',
                'password',
                'phone_number',

            ), 
        }),
        ('Status', {
            "fields": (
                'is_active',
            ), 
        }),
        ("Permissions", {
            "fields": (
                'is_superuser',
                'is_admin',
                'is_staff',
            ), 
        }),
        ("Special Permissions", {
            "fields": (
                'user_permissions',
            ), 
        }),
    )
admin.site.register(User, CustomUserAdmin)