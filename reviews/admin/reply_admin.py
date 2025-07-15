# admin/reply_admin.py
from django.contrib import admin
from ..models import Reply

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'review_id', 'like_count', 'timestamp')
    list_filter = ('user_id', 'review_id')
    search_fields = ('user_id__username', 'review_id__id')
    ordering = ('-timestamp',)

    def like_count(self, obj):
        return obj.likes.count()
    like_count.short_description = 'Likes'
