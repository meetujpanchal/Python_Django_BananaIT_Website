from dataclasses import fields
from django import forms
from .models import Tblenquiry

class Contact_us_form(forms.ModelForm):
    class Meta:
        model = Tblenquiry
        fields = ['name','email','description']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }