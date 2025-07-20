from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from ..models import Department

from django.contrib import admin
from ..models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_id', 'name', 'faculty_link') 
    list_filter = ('faculty',)
    search_fields = ('name', 'faculty__name')
    ordering = ('name',)

    def faculty_link(self, obj):
        if obj.faculty:
            url = reverse('admin:professors_faculty_change', args=[obj.faculty.faculty_id])
            return format_html(
                '<a href="{}">{}: {}</a>', 
                url, 
                obj.faculty.faculty_id, obj.faculty.name)
        
        return "-"
    
    faculty_link.short_description = 'Faculty'
    faculty_link.admin_order_field = 'faculty' 