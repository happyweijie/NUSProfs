from django.urls import path
from . import views

urlpatterns = [
    path("<int:prof_id>", views.professor, name="professor"),
    path("<int:prof_id>/review_summary", views.ReviewSummaryView.as_view(), name='professor_reviews'),
    path('search', views.search, name='search'),
    path('faculties', views.faculties, name='faculties'),
    path('modules', views.ModuleDisplayView.as_view(), name='modules'),
]