# класс Dog, с методом bark, который печатает 'bow-wow'
# и создадим экземляр класса

class Dog:
    color = None

    def bark(self):
        print(f'{self} says: bow-wow')

    def set_color(self, color):
        self.color = color


white_bim_black_ear = Dog()
white_bim_black_ear.bark()
print(white_bim_black_ear.color)
white_bim_black_ear.set_color('black')
print(white_bim_black_ear.color)



