from django.db import models
from .professor import Professor
from .module import Module

class Teaches(models.Model):
    prof = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='teaching')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='taught_by')
    semester = models.CharField(max_length=20)

    class Meta:
        unique_together = ('prof', 'module', 'semester')

    def __str__(self):
        return f"{self.prof.name} taught {self.module.module_code} in {self.semester}"