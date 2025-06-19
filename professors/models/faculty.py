from django.db import models

# ===== Faculty and Department =====
class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.faculty_id}: {self.name}"
