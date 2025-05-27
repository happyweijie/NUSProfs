from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("professor/", views.all_professors, name="all_professors"),
    path("professor/<int:prof_id>/", views.professor, name="professor"),
    path('search/', views.search, name='search'),
]