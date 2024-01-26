from django import forms
from listings.models import Band
from listings.models import Singers

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class MusicForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'


class SingerForm(forms.ModelForm):

    class Meta:
        model = Singers
        fields = '__all__'
