from stocks.models import Toy, Basket, Users
from rest_framework import serializers


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ["pk", "name", "price", "dicription"]


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Users
        # Поля, которые мы сериализуем
        fields = ["pk", "user_name", "login", "password"]


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Basket
        # Поля, которые мы сериализуем
        fields = ["pk", "user_id", "toy_id", "number_of_toys"]
