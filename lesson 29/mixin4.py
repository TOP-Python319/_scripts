class MushromMixin:
    def add_mushrooms(self):
        self.price += 3
        self.toppings.append('mushrooms')


class TomatoMixin:
    def add_tomato(self):
        self.price += 2
        self.toppings.append('tomato')


class OnionMixin:
    def add_onion(self):
        self.price += 1
        self.toppings.append('onion')


class OliveMixin:
    def add_olive(self):
        self.price += 5
        self.toppings.append('olive')


class BaconMixin:
    def add_bacon(self):
        self.price += 4
        self.toppings.append('bacon')


class PineappleMixin:
    def add_pineapple(self):
        self.price += 6
        self.toppings.append('pineapple')


class BasePizza:
    BASE_PIZZA_PRICE = 10

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.toppings = ['cheese']

    def __str__(self):
        return f'{self.name} with {self.toppings}: price ${self.price}'
    

class MushroomPineappleOnionPizza(BasePizza, MushromMixin, PineappleMixin, OnionMixin):
    def __init__(self):
        super().__init__('Mushroom Pineapple Onion', BasePizza.BASE_PIZZA_PRICE)
        self.add_mushrooms()
        self.add_pineapple()
        self.add_onion()

class MushroomTomatoOnionPizza(BasePizza, MushromMixin, TomatoMixin, OnionMixin):
    def __init__(self):
        super().__init__('Mushroom Tomato Onion', BasePizza.BASE_PIZZA_PRICE)
        self.add_mushrooms()
        self.add_tomato()
        self.add_onion()


mpl_pizza = MushroomPineappleOnionPizza()
print(mpl_pizza)

mto_pizza = MushroomTomatoOnionPizza()
print(mto_pizza)