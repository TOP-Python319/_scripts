# полиморфизм в операциях
# num1 = 1
# num2 = 2
# print(num1 + num2)

# str1 = 'Hello'
# str2 = 'Python!'
# print(str1 + str2)


# полиморфизм в функциях
# print(len('string'))
# print(len(['l', 'i', 's', 't']))
# print(len({'a': 1, 'b': 2, 'c': 3}))


# полиморфизм в методах

class Cat:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f'I am a cat. My name is {self.name}')

    def make_sound(self):
        print(f'{self.name} meows.')


class Dog:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f'I am a dog. My name is {self.name}')

    def make_sound(self):
        print(f'{self.name} barks.')


whiskers = Cat('Whiskers')
fluffy = Dog('Fluffy')
tom = Dog('Tom')
scooby = Cat('Scooby')
matroskin = Dog('Matroskin')

for animal in [whiskers, fluffy, tom, scooby, matroskin]:
    animal.info()
    animal.make_sound()


