from django import forms
from .models import ColTypes

class ColTypesForm(forms.ModelForm):
    class Meta:
        model = ColTypes
        fields = ['ColType']
