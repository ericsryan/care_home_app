from django.contrib import admin

from .models import Client, Doctor, Medication, Prescription

admin.site.register(Client)
admin.site.register(Doctor)
admin.site.register(Medication)
admin.site.register(Prescription)
