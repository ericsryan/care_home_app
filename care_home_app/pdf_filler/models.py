from django.db import models


class FillablePDF(models.Model):
    name = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to='fillable_pdfs/')
