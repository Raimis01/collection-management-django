from django.db import models
from django.core.validators import MaxValueValidator

class Statuses(models.Model):
    Status = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return str(self.Status)
