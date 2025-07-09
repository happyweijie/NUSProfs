from django.db import models

class Semester(models.Model):
    SEMESTER_CHOICES = [
        (1, 'Semester 1'),
        (2, 'Semester 2'),
    ]

    ay_start = models.IntegerField() # Academic year start
    semester_number = models.IntegerField(choices=SEMESTER_CHOICES)

    class Meta:
        unique_together = ('ay_start', 'semester_number')
        ordering = ['-ay_start', '-semester_number']

    @classmethod
    def latest_academic_year(cls):
        """Return the latest 2 semesters"""
        return list(cls.objects.all().order_by('-ay_start', 'semester_number')[:2])
    
    @classmethod
    def get_academic_year(cls, year):
        """Return the semesters for a given academic year"""
        return list(cls.objects.filter(ay_start=year).order_by('-ay_start', 'semester_number'))
    
    @classmethod
    def format_ay(cls, year):
        start = int(year) % 100
        end = start + 1
        return f"AY{start:02}/{end:02}"
    
    def __str__(self):
        return f"{Semester.format_ay(self.ay_start)} Semester {self.semester_number}"
