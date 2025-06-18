from django.urls import path
from . import views

urlpatterns =[
    path("users/", views.UserReviewListView.as_view(), name="my_reviews"),
    path("users/<str:username>", views.UserReviewListView.as_view(), name="user_reviews"),
    path("professors/<int:prof_id>", views.ProfessorReviewsView.as_view(), name="prof_reviews"),
    path("create", views.ReviewCreateView.as_view(), name="create_review"),
    path("<int:pk>/edit", views.ReviewUpdateView.as_view(), name="edit_review"),
    path("<int:pk>/delete", views.ReviewDeleteView.as_view(), name="delete_review"),
    path("<int:pk>/reply", views.ReplyCreateView.as_view(), name="create_reply"),
    path("<int:review_id>/replies", views.ReplyDisplayView.as_view(), name="display_replies"),
    path("<int:pk>/like", views.ReviewLikeToggleView.as_view(), name="like_review"),
    path("reply/<int:pk>/edit", views.ReplyUpdateView.as_view(), name="edit_reply"),
    path("reply/<int:pk>/delete", views.ReplyDeleteView.as_view(), name="delete_reply"),
    path("reply/<int:pk>/like", views.ReplyLikeToggleView.as_view(), name="like_reply"),
]
