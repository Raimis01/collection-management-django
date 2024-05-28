from django import forms
from .models import Collectables, Albums
from owner_page.models import Users

class CollectablesForm(forms.ModelForm):
    Price = forms.DecimalField(max_digits=10, decimal_places=2, required=False)

    class Meta:
        model = Collectables
        fields = ['Name', 'Country', 'Description', 'Year', 'Condition', 'Status', 'Material', 'ColType', 'CurrValue', 'CurrType', 'AlbLoc', 'Owner']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CollectablesForm, self).__init__(*args, **kwargs)


        self.fields['Year'].required = True
        self.fields['ColType'].required = True
        self.fields['Country'].required = True

        optional_fields = ['Name', 'Description', 'Condition', 'Status', 'Material', 'CurrValue', 'CurrType', 'AlbLoc', 'Owner']
        for field in optional_fields:
            self.fields[field].required = False


        if user and not user.is_superuser:
            self.fields['Owner'].widget = forms.HiddenInput()
            self.fields['Owner'].initial = user
            self.fields['AlbLoc'].queryset = Albums.objects.filter(OwnId=user)
        else:
            self.fields['Owner'].queryset = Users.objects.all()
            self.fields['AlbLoc'].queryset = Albums.objects.all()