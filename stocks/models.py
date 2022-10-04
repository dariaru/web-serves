from django.db import models

class Toy(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    dicription = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'toys'


class Users(models.Model):
    user_name = models.CharField(max_length=50, verbose_name="Имя пользователя")
    login = models.CharField(max_length=50, verbose_name="Логин")
    password = models.CharField(max_length=50, verbose_name="Пароль")

    class Meta:
        managed = False
        db_table = 'users'


class Basket(models.Model):
    user_id = models.IntegerField(max_length=11)
    toy_id = models.IntegerField(max_length=11)
    number_of_toys = models.IntegerField(max_length=20)

    class Meta:
        managed = False
        db_table = 'basket'