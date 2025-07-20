from django.contrib import admin
from ..models import Professor

from django.utils.html import format_html
from django.urls import reverse

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('prof_id', 'name', 'title', 'department_link', 
                    'average_rating_display', 'review_count_display')
    list_filter = ('department', 'title')
    search_fields = ('name', 'title', 'department__name')
    ordering = ('name',)

    def department_link(self, obj):
        if obj.department:
            url = reverse('admin:professors_department_change', args=[obj.department.dept_id])
            return format_html('<a href="{}">{}</a>', url, obj.department.name)
        return "-"
    department_link.short_description = 'Department'
    department_link.admin_order_field = 'department'

    def average_rating_display(self, obj):
        return obj.average_rating()
    average_rating_display.short_description = 'Avg. Rating'

    def review_count_display(self, obj):
        return obj.review_count()
    review_count_display.short_description = 'Review Count'
