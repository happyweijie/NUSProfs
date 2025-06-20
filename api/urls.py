from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("demo", views.search_demo, name="demo"),
    path("demo2", views.faculties_demo, name="demo2"),
    path("professor/<int:prof_id>", views.professor, name="professor"),
    path('search', views.search, name='search'),
    path('faculties', views.faculties, name='faculties'),
    path('professor/<int:prof_id>/review_summary', views.ReviewSummaryView.as_view(), name='professor_reviews')
]