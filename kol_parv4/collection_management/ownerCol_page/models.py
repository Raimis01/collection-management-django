from django.db import models
from django.core.validators import MaxValueValidator
from collectables_page.models import Collectables
from colType_page.models import ColTypes
from owner_page.models import Users



class OwnersCol(models.Model):
    ColType = models.ForeignKey(ColTypes, on_delete=models.CASCADE, null=False)
    Owner = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)

