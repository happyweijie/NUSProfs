from django.db import models
from django.db.models import Q

# Results for search results for Professors
class ProfessorQuerySet(models.QuerySet):
    def filter_by_name_dept_faculty(self, name_query, department_ids=None, faculty_ids=None):
        filters = Q(name__icontains=name_query)

        if department_ids or faculty_ids:
            department_ids = department_ids or []
            faculty_ids = faculty_ids or []
            department_filter = Q(department_id__in=department_ids)
            faculty_filter = Q(department__faculty_id__in=faculty_ids)
            filters &= (department_filter | faculty_filter)

        return self.filter(filters)
    