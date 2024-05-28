from django.db import models
from django.core.validators import MaxValueValidator

class Materials(models.Model):
    Material = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return str(self.Material)
