# без абстрактного класса
# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print(f'{self.name} barks.')


# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print(f'{self.name} meows.')


# class Bird:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print(f'{self.name} chirps.')


# с абстрактным классом
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print(f'{self.name} barks.')


class Cat(Animal):
    def make_sound(self):
        print(f'{self.name} meows.')


class Bird(Animal):
    def make_sound(self):
        print(f'{self.name} chirps.')


d = Dog('Fluffy')
c = Cat('Garfield')
b = Bird('Woofer')

for animal in (d, c, b):
    animal.make_sound()
