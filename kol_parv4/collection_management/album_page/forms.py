from django import forms
from .models import Albums
from owner_page.models import Users


class AlbumsForm(forms.ModelForm):
    class Meta:
        model = Albums
        # fields = ['AlbLocId', 'Name', 'Page', 'PageRow', 'PageCol', 'OwnId']
        fields = ['Name', 'Page', 'PageRow', 'PageCol', 'OwnId'] 

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AlbumsForm, self).__init__(*args, **kwargs)
        if user and not user.is_superuser:
            self.fields['OwnId'].widget = forms.HiddenInput()
            self.fields['OwnId'].initial = user
        else:
            self.fields['OwnId'].queryset = Users.objects.all()

class DeleteAlbumForm(forms.Form):
    album_name = forms.CharField(label='Album Name', max_length=100)
    user = forms.ModelChoiceField(queryset=Users.objects.all(), label='User', required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DeleteAlbumForm, self).__init__(*args, **kwargs)
        if not self.user.is_superuser:
            self.fields['user'].widget = forms.HiddenInput()
            self.fields['user'].initial = self.user
