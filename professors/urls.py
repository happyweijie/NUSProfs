from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.all_professors, name="all_professors"),
]