from django.contrib import admin
from ..models import Semester

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('academic_year_display', 'semester_number')
    list_filter = ('semester_number',)
    ordering = ('-ay_start', '-semester_number')
    search_fields = ('ay_start',)

    def academic_year_display(self, obj):
        return obj.format_ay(obj.ay_start)
    academic_year_display.short_description = 'Academic Year'
