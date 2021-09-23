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
    return render(
        request,
        'profiles/edit_profile.html',
        {'form': form, 'edit_name': 'Client'}
        )


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
    doctors = models.Doctor.objects.filter(client__pk=pk)
    return render(
        request,
        'profiles/view_client_profile.html',
        {'client': client, 'doctors': doctors}
        )


@login_required
def view_client_list(request):
    """List of all clients."""
    clients = models.Client.objects.filter(current_client=True)
    return render(request, 'profiles/client_list.html', {'clients': clients})


@login_required
def create_doctor_profile(request):
    """Create new Doctor profile."""
    form = forms.DoctorCreationForm()
    if request.method == 'POST':
        form = forms.DoctorCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'profiles/create_doctor_profile.html', {'form': form})


@login_required
def edit_doctor_profile(request, pk):
    """Edit a Doctor's profile."""
    doctor = models.Doctor.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.DoctorUpdateForm(
            request.POST,
            instance=doctor
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profiles:doctor_profile',
                                                args=[doctor.id]))
    else:
        form = forms.DoctorUpdateForm(instance=doctor)
    return render(
        request,
        'profiles/edit_profile.html',
        {'form': form, 'edit_name': 'Doctor'}
        )


@login_required
def view_doctor_profile(request, pk):
    """Show the details of a doctor's profile."""
    doctor = get_object_or_404(models.Doctor, id=pk)
    clients = models.Client.objects.filter(doctors__pk=pk)
    return render(
        request,
        'profiles/view_doctor_profile.html',
        {'doctor': doctor, 'clients': clients}
        )


@login_required
def view_doctor_list(request):
    """List of all doctors."""
    doctors = models.Doctor.objects.all()
    return render(request, 'profiles/doctor_list.html', {'doctors': doctors})


@login_required
def create_medication(request):
    form = forms.MedicationCreationForm()
    if request.method == 'POST':
        form = forms.MedicationCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'profiles/create_medication.html', {'form': form})


@login_required
def edit_medication_profile(request, pk):
    """Edit a medication profile."""
    medication = models.Medication.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.MedicationUpdateForm(
            request.POST,
            instance=medication
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profiles:medication_profile',
                                                args=[medication.id]))
    else:
        form = forms.MedicationUpdateForm(instance=medication)
    return render(
        request,
        'profiles/edit_profile.html',
        {'form': form, 'edit_name': 'Medication'}
        )


@login_required
def view_medication_profile(request, pk):
    """Show the details of a medication profile."""
    medication = get_object_or_404(models.Medication, id=pk)
    return render(
        request,
        'profiles/view_medication_profile.html',
        {'medication': medication}
        )


@login_required
def view_medication_list(request):
    """List of all medications."""
    medications = models.Medication.objects.all()
    return render(
        request,
        'profiles/medication_list.html',
        {'medications': medications}
        )
