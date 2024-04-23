# __init__ магический метод, который вызывается при создании экземпляра класса
# так же называется методом конструктором


class Car:

    # метод конструктор, вызывается в момент создания ЭК
    # на самом деле метод __init__ сначала запускает магический метод __new__
    def __init__(self, make, engine):
        self.make = make
        self.engine = engine

    # метод __repr__ вызывается при вызове print на ЭК
    def __repr__(self) -> str:
        return f"{self.make} {self.engine}"
    

nissan = Car("Juke", "1.6")
print(nissan)
print(nissan.__dict__)


# не указали атрибуты, поэтому ошибка
# toyota = Car()
# >>>: TypeError: Car.__init__() missing 2 required positional arguments: 'make' and 'engine'

