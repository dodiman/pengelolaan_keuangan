from django import forms
from .models import *

class PengeluaranForm(forms.ModelForm):
    class Meta:
        model = Pengeluaran
        # fields = "__all__"
        exclude = ['user']

class PengeluaranDetailForm(forms.ModelForm):
    class Meta:
        model = DetailPengeluaran
        fields = "__all__"