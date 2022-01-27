from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=128, verbose_name='Название ресторана')
    street = models.CharField(max_length=128, null=True, blank=True,
                              verbose_name='Название улицы')
    number_house = models.IntegerField(null=True, blank=True,
                                       verbose_name='Номер дома')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']


class Ingredients(models.Model):
    name = models.CharField(max_length=128,
                            verbose_name='Название ингридиента')


class Pizza(models.Model):
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='pizza',
                                   verbose_name='Ресторан')
    name = models.CharField(max_length=128, verbose_name='Название пиццы')
    ingredients = models.ManyToManyField(Ingredients, related_name='pizza',
                                         verbose_name='Ингридиенты')
    pastry = models.CharField(max_length=128, verbose_name='Толщина теста')
    secret_ingredient = models.CharField(max_length=128,
                                         verbose_name='Секретный ингридиент')


class People(models.Model):
    iin = models.CharField(max_length=12, verbose_name='ИИН')
