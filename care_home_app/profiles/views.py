from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import forms
from . import models

def create_client_profile(request):
    """Create new Client profile"""
    form = forms.ClientCreationForm()
    if request.method == 'POST':
        form = forms.ClientCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'profiles/create_client_profile.html', {'form': form})


def edit_client_profile(request, pk):
    """Edit Client profile"""
    client = models.Client.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.ClientUpdateForm(
            request.POST,
            instance=client
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = forms.ClientUpdateForm(instance=client)
    return render(request, 'profiles/edit_client_profile.html', {'form': form})


def delete_profile(request):
    """Delete profile"""
    pass


def view_client_profile(request, pk):
    """Show the details of a client profile"""
    client = get_object_or_404(models.Client, id=pk)
    return render(request, 'profiles/view_client_profile.html', {'client': client})
