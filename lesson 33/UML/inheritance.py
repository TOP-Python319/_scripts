class Animal:

    def __init__(self, name: str):
        self.name = name

    def speak(self):
        print(f'{self.name} speaks something.')


class Dog(Animal):

    def speak(self):
        print(f'{self.name} speaks bow.')


class Cat
    def speak(self):
        print(f'{self.name} speaks meow.')