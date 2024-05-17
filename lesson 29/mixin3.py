class SalaryMixin:
    def __init__(self, salary):
        self.salary = salary

    def calculate_pay(self, hours_worked):
        return self.salary * hours_worked


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Привет, меня зовут {self.name} и мне {self.age} лет')


class Employee(Person, SalaryMixin):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        SalaryMixin.__init__(self, salary)
    
    def say_hello(self):
        print(f'Привет, меня зовут {self.name} и мне {self.age} лет. Моя зарплата составляет {self.salary}')

    
class Manager(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

    def say_hello(self):
        print(f'Привет, меня зовут {self.name} и мне {self.age} лет. Моя зарплата составляет {self.salary} и я менеджер')


e = Employee('Иван', 25, 50000)
e.say_hello()
print(Employee.mro())

m = Manager('Петя', 30, 100000)
m.say_hello()