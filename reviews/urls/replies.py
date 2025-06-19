from django.urls import path
from reviews.views.replies import (
    ReplyCreateView,
    ReplyDisplayView,
    ReplyUpdateView,
    ReplyDeleteView,
    ReplyLikeToggleView,
)

urlpatterns = [
    path("<int:pk>/reply", ReplyCreateView.as_view(), name="create_reply"),
    path("<int:review_id>/replies", ReplyDisplayView.as_view(), name="display_replies"),
    path("reply/<int:pk>/edit", ReplyUpdateView.as_view(), name="edit_reply"),
    path("reply/<int:pk>/delete", ReplyDeleteView.as_view(), name="delete_reply"),
    path("reply/<int:pk>/like", ReplyLikeToggleView.as_view(), name="like_reply"),
]
