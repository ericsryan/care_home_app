# Generated by Django 3.2.5 on 2021-09-23 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_client_prescriptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='prescriptions',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='prescribed_to',
        ),
        migrations.AddField(
            model_name='prescription',
            name='prescribed_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='profiles.client'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='prescribing_dr',
        ),
        migrations.AddField(
            model_name='prescription',
            name='prescribing_dr',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='profiles.doctor'),
            preserve_default=False,
        ),
    ]