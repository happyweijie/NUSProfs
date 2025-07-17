from django.contrib import admin
from ..models import Teaches

@admin.register(Teaches)
class TeachesAdmin(admin.ModelAdmin):
    list_display = ('professor_name', 'module_code', 'semester_display')
    list_filter = ('semester', 'module', 'prof__name')
    search_fields = ('prof__name', 'module__module_code')
    ordering = ('prof__name', 'module__module_code')

    def professor_name(self, obj):
        return obj.prof.name
    professor_name.short_description = 'Professor'

    def module_code(self, obj):
        return obj.module.module_code
    module_code.short_description = 'Module'

    def semester_display(self, obj):
        return str(obj.semester) if obj.semester else "N/A"
    semester_display.short_description = 'Semester'
