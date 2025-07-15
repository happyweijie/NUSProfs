from django.contrib import admin
from ..models import Professor

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('prof_id', 'name', 'title', 'department', 'average_rating_display', 'review_count_display')
    list_filter = ('department', 'title')
    search_fields = ('name', 'title', 'department__name')
    ordering = ('name',)

    def average_rating_display(self, obj):
        return obj.average_rating()
    average_rating_display.short_description = 'Avg. Rating'

    def review_count_display(self, obj):
        return obj.review_count()
    review_count_display.short_description = 'Review Count'
