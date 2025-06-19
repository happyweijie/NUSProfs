from django.urls import path
from ..views.reviews import (
    UserReviewListView,
    ProfessorReviewsView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView,
    ReviewLikeToggleView,
)

urlpatterns = [
    path("users/", UserReviewListView.as_view(), name="my_reviews"),
    path("users/<str:username>", UserReviewListView.as_view(), name="user_reviews"),
    path("professor/<int:prof_id>", ProfessorReviewsView.as_view(), name="prof_reviews"),
    path("create", ReviewCreateView.as_view(), name="create_review"),
    path("<int:pk>/edit", ReviewUpdateView.as_view(), name="edit_review"),
    path("<int:pk>/delete", ReviewDeleteView.as_view(), name="delete_review"),
    path("<int:pk>/like", ReviewLikeToggleView.as_view(), name="like_review"),
]
