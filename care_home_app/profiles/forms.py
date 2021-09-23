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
            'doctors',
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


class MedicationCreationForm(forms.ModelForm):
    """Form to create a new medication."""

    class Meta:
        model = models.Medication
        fields = (
            'name',
            'strength',
        )


class MedicationUpdateForm(forms.ModelForm):
    """Form to update an existing medication."""

    class Meta:
        model = models.Medication
        fields = (
            'name',
            'strength',
        )


class PrescriptionCreationForm(forms.ModelForm):
    """Form to create a new prescription."""

    class Meta:
        model = models.Prescription
        fields = (
            'medication',
            'rx_instructions',
            'prescribing_dr',
            'prescribed_to',
        )


class PrescriptionUpdateForm(forms.ModelForm):
    """Form to update an existing prescription."""

    class Meta:
        model = models.Prescription
        fields = (
            'medication',
            'rx_instructions',
            'prescribing_dr',
            'prescribed_to',
        )


class NewBodyWeightForm(forms.ModelForm):
    """Create new bodyweight record."""

    class Meta:
        model = models.BodyWeight
        fields = (
            'weight',
        )
