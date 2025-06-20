from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("demo", views.search_demo, name="demo"),
    path("demo2", views.faculties_demo, name="demo2"),
]