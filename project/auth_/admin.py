from django.contrib import admin
from .models import MainUser, Client, Card, Profile
# Register your models here.

admin.site.register(MainUser)
admin.site.register(Client)
admin.site.register(Card)
admin.site.register(Profile)
