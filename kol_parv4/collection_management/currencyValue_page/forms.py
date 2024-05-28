from django import forms
from .models import CurrencyValues

class CurrencyValuesForm(forms.ModelForm):
    class Meta:
        model = CurrencyValues
        fields = ['CurrValueId']
