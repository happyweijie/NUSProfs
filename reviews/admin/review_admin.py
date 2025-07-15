from django.contrib import admin
from ..models import Review, Reply

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'prof_id', 'module_code', 'rating', 'text',
                    'reply_count', 'like_count', 'timestamp')
    list_filter = ('rating', 'module_code', 'prof_id')
    search_fields = ('user_id__username', 'prof_id__name', 'module_code__module_code')
    ordering = ('-timestamp',)
    
    def like_count(self, obj):
        return obj.likes.count()
    like_count.short_description = 'Likes'
