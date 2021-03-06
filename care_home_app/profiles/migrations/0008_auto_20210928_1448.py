# Generated by Django 3.2.5 on 2021-09-28 21:48

from django.db import migrations, models
import thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_bodyweight'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='sex',
            field=models.CharField(default='None', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='portrait',
            field=thumbnails.fields.ImageField(default='images/default.jpeg', upload_to='images'),
        ),
    ]
