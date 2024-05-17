# базовый класс Person
#     методы
#         __init__ - имя и номер паспорта
#         display - печатать имя и паспорт
# 
# 
# дочерний класс Employee
#     метод __init__ - имя, номер паспорта, зарплату, отдел


class Person:
    def __init__(self, name, passport):
        self.name = name
        self.passport = passport

    def display(self):
        print(f'{self.name} {self.passport}')


class Employee(Person):
    def __init__(self, name, passport, salary, department):
        super().__init__(name, passport)
        self.salary = salary
        self.department = department


e = Employee('ivan', '3333333333', 3333333333, 404)
e.display()
print(e.salary)
print(e.department)
