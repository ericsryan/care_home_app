from django import forms

from . import models

class ClientCreationForm(forms.ModelForm):
    """Form to add a new client."""
    class Meta:
        model = models.Client
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'portrait',
            'dob',
            'admission_date',
            'address',
        )


class ClientUpdateForm(forms.ModelForm):
    """Form to update details of a client profile."""
    class Meta:
        model = models.Client
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'portrait',
            'dob',
            'admission_date',
            'address',
        )


class DoctorCreationForm(forms.ModelForm):
    """Form to add a new doctor."""
    class Meta:
        model = models.Doctor
        fields = (
            'first_name',
            'last_name',
            'suffix',
            'specialty',
            'address',
            'phone',
        )


class DoctorUpdateForm(forms.ModelForm):
    """Form to update details of a client profile"""
    class Meta:
        model = models.Doctor
        fields = (
            'first_name',
            'last_name',
            'suffix',
            'specialty',
            'address',
            'phone',
        )
