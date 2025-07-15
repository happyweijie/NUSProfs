from django.db import models
from .professor import Professor
from .module import Module
from .semester import Semester

class Teaches(models.Model):
    prof = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='teaching')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='taught_by')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, 
                                 related_name='modules_offered', null=True, blank=True)

    class Meta:
        verbose_name = "Teaching Record"
        verbose_name_plural = "Teaching Records"
        unique_together = ('prof', 'module', 'semester')

    def __str__(self):
        return f"{self.prof.name} taught {self.module.module_code} in {self.semester}"