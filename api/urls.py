from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("professor/<int:prof_id>/", views.professor, name="professor"),
    path('search/', views.search, name='search'),
    path('faculties/', views.faculties, name='faculties'),
]