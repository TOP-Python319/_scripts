class FlyingMixin:
    def fly(self):
        print(f'{self.name} летает')


class BitingMixin:
    def byte(self):
        print(f'{self.name} кусает')


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'f{self.name} ест')

    def sleep(self):
        print(f'{self.name} спит')


class Dog(Animal, BitingMixin):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f'{self.name} лает')


class Cat(Animal, BitingMixin):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        print(f'{self.name} мяукает')


class Bat(Animal, FlyingMixin, BitingMixin):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan


class Bird(Animal, FlyingMixin):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan