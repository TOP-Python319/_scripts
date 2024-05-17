class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def walk(self):
        print('Человек идёт')


class Doctor(Person):
    # def __init__(self, name, lastname, age):
    #     self.name = name
    #     self.lastname = lastname
    #     self.age = age

    def __init__(self, name, lastname, age):
        super().__init__(name, lastname)
        self.age = age

    def walk(self):
        print('Доктор идёт')
        super().walk()


d = Doctor('John', 'Dorian', 30)

d.walk()