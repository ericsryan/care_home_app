from django.db import models


class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=255, blank=True)
    specialty = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.suffix}'


class Client(models.Model):
    """Personal details for a care home client."""
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    portrait = models.ImageField(default='images/default.jpeg', upload_to='images')
    dob = models.DateField()
    admission_date = models.DateField()
    address = models.CharField(max_length=255)
    doctors = models.ManyToManyField(Doctor, blank=True)
    current_client = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
