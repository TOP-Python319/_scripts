class Doctor:
    def can_cure(self):
        print('Могу лечить')

    # def can_build(self):
    #     print('Я тоже могу строить')


class Builder:
    def can_build(self):
        print('Могу строить')


class Person(Builder, Doctor):
    def can_build(self):
        super().can_build()


p = Person()
# p.can_cure()
p.can_build()
print(p)


print(Person.__mro__)