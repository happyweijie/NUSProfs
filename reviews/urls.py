from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("create", views.ReviewCreateView.as_view(), name="create_review"),
    path("<int:pk>/edit", views.ReviewUpdateView.as_view(), name="edit_review"),
    path("<int:pk>/delete", views.ReviewDeleteView.as_view(), name="delete_review"),
    path("<int:pk>/reply", views.ReplyCreateView.as_view(), name="create_reply"),
    path("reply/<int:pk>/edit", views.ReplyUpdateView.as_view(), name="edit_reply"),
    path("reply/<int:pk>/delete", views.ReplyDeleteView.as_view(), name="delete_reply"),
]
