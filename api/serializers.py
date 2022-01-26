from collections import OrderedDict

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import Ingredients, Pizza

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=128, write_only=True)
    street = serializers.CharField(max_length=128, write_only=True)
    number_house = serializers.IntegerField(write_only=True)
    password = serializers.CharField(max_length=128, required=True,
                                     write_only=True)
    address = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'name', 'address', 'username', 'password', 'street',
                  'number_house')

    # Вывод адреса
    def get_address(self, obj):
        return f'{obj.street}, {obj.number_house}'

    # Проверка соотвествия пароля
    def validate_password(self, data):
        validate_password(password=data, user=User)
        return data

    # Создание аккауна пользователя
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredients
        fields = '__all__'


# Сериализатор для вывода пиццы
class PizzasShowSerializer(serializers.ModelSerializer):
    restaurant = UserSerializer()
    '''ingredients = IngredientSerializer(many=True)'''
    ingredients = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Pizza
        fields = '__all__'


# CRUD операции над пиццей
class PizzaSerializer(serializers.ModelSerializer):
    ingredients = serializers.ListField()

    class Meta:
        model = Pizza
        fields = ['name', 'pastry', 'ingredients', 'secret_ingredient']

    def validate_ingredients(self, data):
        print(data)
        for num in range(len(data)):
            print(data[num])
            tmp, _ = Ingredients.objects.get_or_create(name=data[num])
            data[num] = tmp
        return data

    # Демонстрация рецепта
    def to_representation(self, data):
        # передаем контекст для получения тикущего пользователя
        fields = PizzasShowSerializer(data, context=self.context)
        return OrderedDict(fields.data)
