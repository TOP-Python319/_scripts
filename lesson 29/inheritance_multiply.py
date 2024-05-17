# множественное наследование
# MRO (method resolution order), порядок разрешения методов: c3-линеаризация
# class Child(BaseClass1, BaseClass2, BaseClass3)


class Doctor:
    def can_cure(self):
        print('Могу лечить')

    def can_build(self):
        print('Я тоже могу строить')


class Builder:
    def can_build(self):
        print('Могу строить')


class Person(Doctor, Builder):
    pass


p = Person()
p.can_cure()
p.can_build()
print(p)


print(Person.__mro__)