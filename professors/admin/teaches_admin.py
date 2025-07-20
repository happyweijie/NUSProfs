from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from ..models import Teaches

@admin.register(Teaches)
class TeachesAdmin(admin.ModelAdmin):
    list_display = ('professor_link', 'module_link', 'semester_display')
    list_filter = ('semester', 'module', 'prof__name')
    search_fields = ('prof__name', 'module__module_code')
    ordering = ('prof__name', 'module__module_code')

    def professor_link(self, obj):
        if obj.prof:
            url = reverse('admin:professors_professor_change', args=[obj.prof.prof_id])
            return format_html('<a href="{}">{}</a>', url, obj.prof.name)
        return "-"
    professor_link.short_description = 'Professor'
    professor_link.admin_order_field = 'prof__name'

    def module_link(self, obj):
        if obj.module:
            url = reverse('admin:professors_module_change', args=[obj.module.module_code])
            return format_html('<a href="{}">{}</a>', url, obj.module.module_code)
        return "-"
    module_link.short_description = 'Module'
    module_link.admin_order_field = 'module__module_code'

    def semester_display(self, obj):
        return str(obj.semester) if obj.semester else "N/A"
    semester_display.short_description = 'Semester'

