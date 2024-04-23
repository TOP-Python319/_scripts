class Car:
    color = 'red'
    engine = 4.0

    def drive():
        print('!!!drive!!!')


print(Car.__dict__)
# >>>: {'__module__': '__main__', 'color': 'red', 'engine': 4.0, 'drive': <function Car.drive at 0x7fe635886200>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}
# 'drive представляет из себя атрибут-функцию определённую в классе Car
# 'drive': <function Car.drive at 0x7fe635886200>

Car.drive()
# >>>: !!!drive!!!


# чтобы вызвать атрибут-функция, нужно указать имя класса и сам атрибут-функцию:
# Class.method()