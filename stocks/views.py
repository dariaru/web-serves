from django.shortcuts import render
from rest_framework import viewsets
from stocks.serializers import ToySerializer, UsersSerializer, BasketSerializer
from stocks.models import Toy, Users, Basket


class ToyViewSet(viewsets.ModelViewSet):
    queryset = Toy.objects.all().order_by('pk')
    serializer_class = ToySerializer  # Сериализатор для модели


class UsersViewSet(viewsets.ModelViewSet):
    # queryset всех пользователей для фильтрации
    queryset = Users.objects.all().order_by('pk')
    serializer_class = UsersSerializer  # Сериализатор для модели


class BasketViewSet(viewsets.ModelViewSet):
    # queryset всех пользователей для фильтрации
    queryset = Basket.objects.all().order_by('pk')
    serializer_class = BasketSerializer  # Сериализатор для модели
