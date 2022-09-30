from rest_framework import serializers
from .models import MainUser, Client, Card


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('id', 'email', 'first_name', 'last_name', 'phone')


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class ClientSerializer(MainUserSerializer):
    class Meta:
        model = Client
        fields = MainUserSerializer.Meta.fields + ('address',)


class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    bio = serializers.CharField()
    birth_date = serializers.DateField()
    user = MainUserSerializer()

