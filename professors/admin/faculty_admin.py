from django.contrib import admin
from ..models import Faculty

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'name')
    search_fields = ('name',)
    ordering = ('faculty_id',)
    
