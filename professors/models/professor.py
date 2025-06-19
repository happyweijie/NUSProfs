from django.db import models
from .department import Department
from ..querysets import ProfessorQuerySet

class Professor(models.Model):
    prof_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='professors')
    title = models.CharField(max_length=150, blank=True, null=True)
    office = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    objects = ProfessorQuerySet.as_manager()

    def average_rating(self):
        return self.reviews. \
            aggregate(models.Avg('rating'))['rating__avg'] or 0.0
    
    def __str__(self):
        return f"{self.name} ({self.title})"