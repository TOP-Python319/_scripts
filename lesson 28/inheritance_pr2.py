# Базовый класс Person:
# методы: 
#     __init__: принимает имя
#     get_name: возвращает имя
#     is_employee: возвращает False

# Подкласс Employee <- Person
#     метод:
#         is_employee: возвращает True


class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


class Employee(Person):
    def is_employee(self):
        return True


e = Employee('Any')
print(e.get_name())
print(e.is_employee())

p = Person('Person')
print(p.get_name())
print(p.is_employee())
