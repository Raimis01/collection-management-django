from django import forms
from .models import ItemPrices

class ItemPricesForm(forms.ModelForm):
    class Meta:
        model = ItemPrices
        fields = ['Price']
