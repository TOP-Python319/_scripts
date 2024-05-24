# геттеры и сеттеры - методы класса, которые мы используем для получения и установки значений атрибутов экземпляра класса

# геттер используется для получения значения атрибута (начинается на get)
# сеттер используется для установки значения атрибута (начинается на set)

import time
from datetime import datetime


class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._phone = None

    def get_name(self):
        print(f'К атрибуту name обращались в {datetime.now()}')
        return self._name

    def get_age(self):
        print(f'К атрибуту age обращались в {datetime.now()}')
        return self._age

    def set_age(self, age):
        print(f'Атрибут age менялся в {datetime.now()}')
        self._age = age

    def set_name(self, name):
        print(f'Атрибут name менялся в {datetime.now()}')
        self._name = name

    def get_phone(self):
        return self._phone

    def set_phone(self, phone):
        if len(phone) == 10 and phone.startswith('+7'):
            self._phone = phone
        else:
            print('Неверный формат номера')


p = Person('John', 25)

print(p.get_name())
time.sleep(5)
p.set_name('Alex')
print(p.get_age())

# >>>: К атрибуту name обращались в 2024-05-24 20:20:11.513424
# >>>: John
# >>>: Атрибут name менялся в 2024-05-24 20:20:16.518726
# >>>: К атрибуту age обращались в 2024-05-24 20:20:16.518797
# >>>: 25

p.set_phone('+712345678')
print(p.get_phone())
# >>>: +712345678
