from django.db import models
from django.utils import timezone
from collectables_page.models import Collectables

class ItemPrices(models.Model):
    ColId = models.ForeignKey(Collectables, on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    TransDate = models.DateTimeField(default=timezone.now)
