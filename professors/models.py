from django.db import models

# ===== Faculty and Department =====
class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.faculty_id}: {self.name}"

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.faculty.name})"

# ===== Professor and Module =====
class Module(models.Model):
    module_code = models.CharField(max_length=15, unique=True, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.module_code}: {self.name}"
    
class Professor(models.Model):
    prof_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='professors')
    title = models.CharField(max_length=150, blank=True, null=True)
    office = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.title})"
    
    def summary(self):
        return {
            "id": self.prof_id,
            "name": self.name,
            "average_rating": 4.50, # Placeholder for average rating
            "faculty": self.department.faculty.name if self.department else None,
            "department": self.department.name if self.department else None,
            "title": self.title,
        }
    
    def serialize(self):
        return {
            "id": self.prof_id,
            "name": self.name,
            "average_rating": 4.50, # Placeholder for average rating
            "faculty": self.department.faculty.name if self.department else None,
            "department": self.department.name if self.department else None,
            "title": self.title,
            "office": self.office,
            "phone": self.phone,
            "teaching": [teaches.serialize() for teaches in self.teaching.all()]
        }

class Teaches(models.Model):
    prof = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='teaching')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='taught_by')
    semester = models.CharField(max_length=20)

    class Meta:
        unique_together = ('prof', 'module', 'semester')

    def serialize(self):
        return {
            "module_code": self.module.module_code,
            "module_name": self.module.name,
            "semester": self.semester
        }

    def __str__(self):
        return f"{self.prof.name} taught {self.module.module_code} in {self.semester}"