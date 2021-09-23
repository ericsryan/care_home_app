from django.db import models

class Client(models.Model):
    """Personal details for a care home client."""
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    portrait = models.ImageField(default='images/default.jpeg', upload_to='images')
    dob = models.DateField()
    admission_date = models.DateField()
    address = models.CharField(max_length=255)
    current_client = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.suffix}'
