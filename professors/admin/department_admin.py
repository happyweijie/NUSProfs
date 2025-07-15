from django.contrib import admin
from ..models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_id', 'name', 'faculty')
    list_filter = ('faculty',)
    search_fields = ('name', 'faculty__name')
    ordering = ('name',)
