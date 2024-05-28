from django.db import models
from django.core.validators import MaxValueValidator

# monetas, banknotes..
class ColTypes(models.Model):
    ColType = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return str(self.ColType)
