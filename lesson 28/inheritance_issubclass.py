# issubclass(class, classinfo)
# class, класс который мы проверяем
# classinfo, класс или кортеж с классами, на пинадлежность кому проверяем


class Person:
    def can_sleep(self):
        print('Я могу спать!')

    def can_eat(self):
        print('Я могу есть!')


class Doctor(Person):
    def can_cure(self):
        print('Я могу лечить')


class Architect(Person):
    def can_buid(self):
        print('Я могу строить')


class Teacher(Person):
    def can_teach(self):
        print('Я могу учить')


class Ortopedist(Doctor):
    ...


print(issubclass(Doctor, Person))  # True
print(issubclass(Person, Doctor))  # False
print(issubclass(Ortopedist, Doctor))  # True
print(issubclass(Ortopedist, Person))  # True
print(issubclass(Ortopedist, Teacher))  # False
print(issubclass(Ortopedist, Architect))  # False
print(issubclass(Ortopedist, (Doctor, Teacher, Architect)))  # True
print(issubclass(Doctor, Ortopedist))  # False
print(issubclass(Ortopedist, Ortopedist))  # True
