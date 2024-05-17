# делегирование
# super().название_метода_родителя()

class Person:
    def walk(self):
        print('Человек идёт')


class Doctor(Person):
    def walk(self):
        print('Доктор идёт')
        super().walk()  # вызов метода родительского ласса в методе дочернего класса


d = Doctor()
d.walk()