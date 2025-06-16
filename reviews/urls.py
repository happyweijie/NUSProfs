from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("create", views.ReviewCreateView.as_view(), name="create_review"),
    path("<int:pk>/edit", views.ReviewUpdateView.as_view(), name="edit_review"),
]
