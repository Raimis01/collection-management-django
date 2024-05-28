from django import forms
from .models import CurrencyTypes

class CurrencyTypesForm(forms.ModelForm):
    class Meta:
        model = CurrencyTypes
        fields = ['CurrType']
