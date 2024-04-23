# __init__ магический метод, который вызывается при создании экземпляра класса
# так же называется методом конструктором


class Car:

    def __new__(cls, *args, **kwargs):
        # 1. сначала создаётся метод __new__, который создаёт ЭК и наследует все методы базового класса
        return super().__new__(cls)

    def __init__(self, make, engine):
        # 2. затем вызывается метод __init__, добавляет атрибуты в созданный ЭК
        self.make = make
        self.engine = engine

    # метод __repr__ вызывается при вызове print на ЭК
    def __repr__(self) -> str:
        return f"{self.make} {self.engine}"
    

nissan = Car("Juke", "1.6")
print(nissan)
print(nissan.__dict__)
