# Для ПО ресторана нужно разработать модуль, помогающий контролировать использование
# фруктов и овощей на кухне.

# Создайте абстрактный класс
# Ingredient с методами get_name() и get_quantity().

# Затем создайте два подкласса Vegetable и Fruit,
# которые наследуют абстрактные методы от Ingredient и реализуют свои собственные
# версии методов get_name() и get_quantity().


from abc import ABC, abstractmethod


class Ingredient(ABC):

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass


class Vegetable(Ingredient):

    def get_name(self):
        return f'Овощ: {self.name}'

    def get_quantity(self):
        return f'{self.quantity} овощей'


class Fruit(Ingredient):

    def get_name(self):
        return f'Фрукт {self.name}'

    def get_quantity(self):
        return f'{self.quantity} фруктов'


carrot = Vegetable("Морковь", 5)
apple = Fruit("Яблоки", 10)

print(carrot.get_name())
print(carrot.get_quantity())

print(apple.get_name())
print(apple.get_quantity())
