from django.db import models
from django.core.validators import MaxValueValidator

# 5, 10, 100, 50
class CurrencyValues(models.Model):
    CurrValueId = models.IntegerField(primary_key=True, unique=True)

    def __str__(self):
        return str(self.CurrValueId)
