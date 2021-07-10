from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    portrait = models.ImageField(default='images/default.jpeg', upload_to='images')
    dob = models.DateField()
    admission_date = models.DateField()
    address = models.CharField(max_length=255)
