from django import forms
from .models import Years

class YearsForm(forms.ModelForm):
    class Meta:
        model = Years
        fields = ['YearId']
