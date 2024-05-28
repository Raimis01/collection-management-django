from django.db import models
from django.core.validators import MaxValueValidator

class Years(models.Model):
    YearId = models.IntegerField(primary_key=True, validators=[MaxValueValidator(9999)], unique=True)

    def __str__(self):
        return str(self.YearId)
