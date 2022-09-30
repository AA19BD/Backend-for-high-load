from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import sys
import os
sys.path.append(os.getcwd())
from .models import Cart
from auth_.models import Client


@receiver(post_save, sender=Client)
def client_created(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(client=instance)
