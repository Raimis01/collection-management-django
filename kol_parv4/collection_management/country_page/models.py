from django.db import models
from django.core.validators import MaxValueValidator

class Countries(models.Model):
    CountryId = models.CharField(primary_key=True, unique=True, max_length=100)
    Name =  models.CharField(max_length=100)

    def __str__(self):
        return str(self.Name)
