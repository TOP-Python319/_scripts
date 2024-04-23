# метод это фунцкция, которая определена внутри класса
# с парой особенностей:
# 1. метод связан с ЭК и вызывается от ЭК
# 2. при вызове метода первым переметром будет передан тот ЭК, от которого был вызван метод



class Car:
    color = 'red'
    engine = 4.0

    # параметр self передается первым при вызове метода
    # назвать параметр можно как угодно, но по PEP8 принято называеть его self
    def drive(self):
        print(f'!!!drive {self}!!!')


nissan = Car()
toyota = Car()
print(nissan.color)
print(nissan.engine)
print()

# Интерпретатор Python автоматически подставит объект, который хранится в переменной nissan
# в вызываемый метод

# эта запись УСЛОВНО равна nissan.drive(self=nissan)
nissan.drive()  # в метод .drive() неявно передаётся параметр self, который будет равен 'nissan'
toyota.drive()
print('nissan:', hex(id(nissan)))
print('toyota:', hex(id(toyota)))

# >>>: !!!drive <__main__.Car object at 0x7faa2c9ebfd0>!!!
# >>>: !!!drive <__main__.Car object at 0x7faa2c9ebfa0>!!!
# >>>: nissan: 0x7faa2c9ebfd0
# >>>: toyota: 0x7faa2c9ebfa0
