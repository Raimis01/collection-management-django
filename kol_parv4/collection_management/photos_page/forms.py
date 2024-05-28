from django import forms
from .models import Photos

class PhotosForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['Photo']
