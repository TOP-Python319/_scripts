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
    # def can_sleep(self):
    #     print('Я могу спать!')

    # def can_eat(self):
    #     print('Я могу есть!')

    # def can_cure(self):
    #     print('Я могу лечить')


d = Doctor()
a = Architect()
t = Teacher()
o = Ortopedist()

d.can_eat()
d.can_sleep()
a.can_eat()
a.can_sleep()
t.can_eat()
t.can_sleep()
print('------')
print(dir(d))
print(dir(a))
print(dir(t))
print('------')
o.can_eat()
o.can_sleep()
o.can_cure()
print('------')
print(dir(o))
