from django import forms

from . import models

class ClientCreationForm(forms.ModelForm):
    """Form to add a new client"""
    class Meta:
        model = models.Client
        fields = (
            'name',
            'portrait',
            'dob',
            'admission_date',
            'address',
        )
