from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("demo/", views.demo, name="demo"),
    path("demo2/", views.demo2, name="demo2"),
    path("professor/<int:prof_id>/", views.professor, name="professor"),
    path('search/', views.search, name='search'),
    path('faculties/', views.faculties, name='faculties'),
]