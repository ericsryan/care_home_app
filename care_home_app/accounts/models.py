from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        UserAccount.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    instance.useraccount.save()


class UserAccount(models.Model):
    """A user profile model that extends the built-in user model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=14, blank=True)
