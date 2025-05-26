from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all/", views.all_professors, name="all_professors"),
    path("<int:prof_id>/", views.professors, name="professors"),
]