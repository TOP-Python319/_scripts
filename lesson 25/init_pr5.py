# класс Person
# атрибуты name, age
# метод, который печатает инфо о человеке

# класс Company
# атрибуты name, location
# метод, который печатает инфо о компании

# класс Employee
# атрибуты personal_data с инфо о Person и work_data с инфо о Company
# в эти атрибуты нужно сохранить экземпляры классов Person и Company
# salary
# position


class Person:
    def __init__(self, name, age, city=None):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f'{self.name} from {self.city}'


class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f'{self.name}'


class Employee:
    def __init__(self, name, age, company_name, location):
        self.personal_data = Person(name, age)
        self.work_data = Company(company_name, location)


tiunov = Employee(
    name='Михаил', 
    age=30,
    company_name='top-academy',
    location='Erevan'
)

tiunov
# >>>: <__main__.Employee object at 0x7fa4599d7fd0>
tiunov.personal_data
# >>>: <__main__.Person object at 0x7fa4599d7cd0>
tiunov.work_data
# >>>: <__main__.Company object at 0x7fa4599d7c40>

print(tiunov.personal_data)
# >>>: Михаил from None
print(tiunov.work_data)
# >>>: top-academy