class Car:
    color = 'red'
    engine = 4.0

    def drive(self):
        print(f'!!!drive {self}!!!')

    def set_color(self, color):
        self.color = color
        print(f'Теперь машина имеет цвет {self.color}')

    def get_color(self):
        print(f'Цвет машины: {self.color}')


nissan = Car()
print(nissan.color)
nissan.set_color('blue')
nissan.get_color()
print(nissan.color)
print()

toyota = Car()
print(toyota.color)
toyota.set_color('green')
toyota.get_color()
print(toyota.color)
print()

jaguar = Car()
print(jaguar.color)