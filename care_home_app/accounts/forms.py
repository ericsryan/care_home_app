from django import forms
from django.contrib.auth.models import User

from . import models


class UserUpdateForm(forms.ModelForm):
    """Form to allow users to update their user information"""
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )


class UserAccountUpdateForm(forms.ModelForm):
    """Form to allow users to update account information."""

    class Meta:
        model = models.UserAccount
        fields = (
            'dob',
            'address',
            'phone',
        )
