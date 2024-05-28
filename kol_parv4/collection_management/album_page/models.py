from django.db import models
from django.core.validators import MaxValueValidator
from owner_page.models import Users

class Albums(models.Model):
    AlbLocId = models.CharField(primary_key=True, unique=True, max_length=100)
    Name = models.CharField(max_length=100)
    Page = models.IntegerField()
    PageRow = models.IntegerField()
    PageCol = models.IntegerField()
    OwnId = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.AlbLocId)
