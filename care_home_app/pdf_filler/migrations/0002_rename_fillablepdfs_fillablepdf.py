# Generated by Django 3.2.5 on 2021-09-27 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_filler', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FillablePDFs',
            new_name='FillablePDF',
        ),
    ]
