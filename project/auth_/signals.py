from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Card, Client, MainUser, Profile


@receiver(post_save, sender=Client)
def user_created_client(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(pre_save, sender=Client)
def client_created(sender, instance, **kwargs):
    instance.card = Card.objects.create()
