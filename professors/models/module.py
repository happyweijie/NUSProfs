from django.db import models

class Module(models.Model):
    module_code = models.CharField(max_length=15, unique=True, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.module_code}: {self.name}"
    
    def save(self, *args, **kwargs):
        self.module_code = self.module_code.upper()
        super().save(*args, **kwargs)