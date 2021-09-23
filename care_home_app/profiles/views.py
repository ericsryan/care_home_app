from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import forms
from . import models


@login_required
def create_client_profile(request):
    """Create new Client profile."""
    form = forms.ClientCreationForm()
    if request.method == 'POST':
        form = forms.ClientCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'profiles/create_client_profile.html', {'form': form})


@login_required
def edit_client_profile(request, pk):
    """Edit Client profile."""
    client = models.Client.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.ClientUpdateForm(
            request.POST,
            request.FILES,
            instance=client
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profiles:client_profile',
                                                args=[client.id]))
    else:
        form = forms.ClientUpdateForm(instance=client)
    return render(request, 'profiles/edit_client_profile.html', {'form': form})


@login_required
def remove_client_profile(request, pk):
    """Set the client profile status to innactive."""
    client = models.Client.objects.get(pk=pk)
    client.current_client=False
    client.save()
    return HttpResponseRedirect(reverse('profiles:client_list'))


@login_required
def view_client_profile(request, pk):
    """Show the details of a client profile."""
    client = get_object_or_404(models.Client, id=pk)
    return render(request, 'profiles/view_client_profile.html', {'client': client})


@login_required
def view_client_list(request):
    """List of all clients."""
    clients = models.Client.objects.filter(current_client=True)
    return render(request, 'profiles/client_list.html', {'clients': clients})
