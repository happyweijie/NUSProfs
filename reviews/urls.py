from django.urls import path, include

urlpatterns = [
    path("", include(("reviews.urls.reviews", "reviews"), namespace="review")),
    path("", include(("reviews.urls.replies", "replies"), namespace="reply")),
]
