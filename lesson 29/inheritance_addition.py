# переопределение метода и расширение класса

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"I'm person {self.name}"


class Doctor(Person):
    def __str__(self):
        return f"I'm doctor {self.name}"

    def walk(self):
        print('Doctor is walking')


p = Person('ivan')
d = Doctor('JD')

print(p)
print(d)

d.walk()
# p.walk()
# AttributeError: 'Person' object has no attribute 'walk'
# Person не имеет атрибута или метода walk. Мы его добавили только в потомке

