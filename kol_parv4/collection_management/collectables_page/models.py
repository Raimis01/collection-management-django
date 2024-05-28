from django.db import models
from django.core.validators import MaxValueValidator
from owner_page.models import Users
from country_page.models import Countries
from year_page.models import Years
from condition_page.models import Conditions
from status_page.models import Statuses
from material_page.models import Materials
from colType_page.models import ColTypes
from currencyValue_page.models import CurrencyValues
from currencyType_page.models import CurrencyTypes
from album_page.models import Albums


class Collectables(models.Model):
    ColId = models.CharField(primary_key=True, unique=True, max_length=100)
    Name = models.CharField(max_length=100)
    Country = models.ForeignKey(Countries, on_delete=models.SET_NULL, null=True)
    Description = models.CharField(max_length=200)
    Year = models.ForeignKey(Years, on_delete=models.SET_NULL, null=True)
    Condition = models.ForeignKey(Conditions, on_delete=models.SET_NULL, null=True)
    Status = models.ForeignKey(Statuses, on_delete=models.SET_NULL, null=True)
    Material = models.ForeignKey(Materials, on_delete=models.SET_NULL, null=True)
    ColType = models.ForeignKey(ColTypes, on_delete=models.SET_NULL, null=True)
    CurrValue = models.ForeignKey(CurrencyValues, on_delete=models.SET_NULL, null=True)
    CurrType = models.ForeignKey(CurrencyTypes, on_delete=models.SET_NULL, null=True)
    AlbLoc = models.ForeignKey(Albums, on_delete=models.SET_NULL, null=True, blank=True)
    Owner = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return str(self.ColId)
