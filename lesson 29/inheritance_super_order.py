class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.age = None

    def walk(self):
        print('Человек идёт')


class Doctor(Person):
    def __init__(self, name, lastname, age):
        super().__init__(name, lastname)  # делегирование
        self.age = age  # логика

    def walk(self):
        print('Доктор идёт')
        super().walk()


d = Doctor('John', 'Dorian', 30)

print(d.name, d.lastname, d.age)


# как правило сначала идёт делегирование,
# а потом логика, чтобы не возникали сайд-эфекты
# и чтобы методы родительского класса не затирали атрибуты потомка