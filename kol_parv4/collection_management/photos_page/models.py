from django.db import models
from collectables_page.models import Collectables
import os
from django.conf import settings

class Photos(models.Model):
    ColId = models.ForeignKey(Collectables, on_delete=models.CASCADE, null=False)
    Photo = models.ImageField(upload_to='collectables_photos/')

    def delete(self, *args, **kwargs):
        if self.Photo:
            photo_path = self.Photo.path
            if os.path.isfile(photo_path):
                os.remove(photo_path)
        super(Photos, self).delete(*args, **kwargs)  


    def __str__(self):
        return self.ColId