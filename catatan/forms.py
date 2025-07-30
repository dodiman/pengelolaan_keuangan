from django import forms
from .models import Catatan

class CatatanForm(forms.ModelForm):
    class Meta:
        model = Catatan
        exclude = ['user']