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


d = Doctor()
a = Architect()
t = Teacher()
o = Ortopedist()

print(isinstance(d, Person))  # True
print(isinstance(a, Person))  # True
print(isinstance(t, Person))  # True
print(isinstance(o, Person))  # True
print(isinstance(d, Doctor))  # True
print(isinstance(a, Architect))  # True
print(isinstance(t, Teacher))  # True
print(isinstance(o, Ortopedist))  # True
print(isinstance(d, Ortopedist))  # False
print(isinstance(o, Doctor))  # True

