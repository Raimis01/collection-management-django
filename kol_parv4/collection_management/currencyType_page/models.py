from django.db import models
from django.core.validators import MaxValueValidator

# euro, cneti, rubli
class CurrencyTypes(models.Model):
    CurrType = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return str(self.CurrType)
