from django import forms
from .models import Statuses

class StatusesForm(forms.ModelForm):
    class Meta:
        model = Statuses
        fields = ['Status']
