from datetime import date
from django.db import models

from thumbnails.fields import ImageField


class Client(models.Model):
    """Personal details for a care home client."""
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    portrait = ImageField(default='images/default.jpeg', resize_source_to='large', upload_to='images')
    sex = models.CharField(max_length=255)
    dob = models.DateField()
    admission_date = models.DateField()
    address = models.CharField(max_length=255)
    doctors = models.ManyToManyField('Doctor', blank=True)
    current_client = models.BooleanField(default=True)
    uci_number = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        return (date.today().year - self.dob.year - ((
                date.today().month,
                date.today().day) < (self.dob.month, self.dob.day)))

    @property
    def full_name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    @property
    def last_name_first(self):
        return f'{self.last_name}, {self.first_name}'


class Doctor(models.Model):
    """Information for client's doctors."""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=255, blank=True)
    specialty = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.suffix}'


class Medication(models.Model):
    """Medication name and strength."""
    name = models.CharField(max_length=255)
    strength = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.strength}'


class Prescription(models.Model):
    """Information for client prescriptions."""
    medication = models.ForeignKey('Medication', on_delete=models.PROTECT)
    rx_instructions = models.TextField()
    prescribing_dr = models.ForeignKey('Doctor', on_delete=models.PROTECT)
    prescribed_to = models.ForeignKey('Client', on_delete=models.PROTECT)

    def __str___(self):
        return f'{self.medication}'


class BodyWeight(models.Model):
    client = models.ForeignKey('Client', on_delete=models.PROTECT)
    weight = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.weight}'
