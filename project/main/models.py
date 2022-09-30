import sys
import os
sys.path.append(os.getcwd())
from django.db import models
from auth_.models import Client



class CartManager(models.Manager):
    def get_client(self):
        return self.get_related().client

    def get_related(self):
        return self.select_related('client')


class Cart(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, null=True)

    objects = CartManager

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return self.id.__str__()
