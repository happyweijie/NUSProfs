from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ..models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # List of fields to display in the user list page
    list_display = ('username', 'email', 'is_staff')

    # Fields to use for searching users in the admin
    search_fields = ('username', 'email')

    # Fields to filter by in the admin list
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    # Fieldsets define the layout of the user detail/edit form in admin
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields shown when creating a new user in admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
