from django.urls import path
from . import views

urlpatterns = [
    path("<int:prof_id>", views.ProfessorDetailsView.as_view(), name="professor"),
    path("<int:prof_id>/review_summary", 
         views.ReviewSummaryView.as_view(), name='professor_reviews'),
    path('search', views.ProfessorSearchView.as_view(), name='search'),
    path('faculties', views.FacultyListView.as_view(), name='faculties'),
    path('modules', views.ModuleDisplayView.as_view(), name='modules'),
]