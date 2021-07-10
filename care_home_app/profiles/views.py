from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import forms
from . import models

def create_client_profile(request):
    """Create new profile"""
    form = forms.ClientCreationForm()
    if request.method == 'POST':
        form = forms.ClientCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'profiles/create_client_profile.html', {'form': form})


def edit_profile(request):
    """Edit profile"""
    pass


def delete_profile(request):
    """Delete profile"""
    pass


def show_profile(request):
    """Show the details of a profile"""
    pass
