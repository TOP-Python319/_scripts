# класс Robot
# два метода say_hello и say_bye
# метод set_name


class Robot:
    
    def set_name(self, name):
        self.name = name
    
    def say_hello(self):
        if hasattr(self, 'name'):  # True/False
            print(f"Hello, I'm {self.name}")
        else:
            print('У робота нет имени.')

    def say_bye(self):
        print('Bye!')

print('R2D2:')
r2d2 = Robot()
r2d2.set_name('r2d2')
r2d2.say_hello()
r2d2.say_bye()
print()
print('C3PO:')
c3po = Robot()
c3po.say_hello()
c3po.say_bye()

