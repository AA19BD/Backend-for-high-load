import sys
import os
sys.path.append(os.getcwd())
from rest_framework import serializers
from .models import Cart
from auth_.serializers import ClientSerializer



class CartSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Cart
        fields = ('products', 'client',)


class GetCartSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Cart
        fields = "__all__"
