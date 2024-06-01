from copy import deepcopy


class Prototype:
    def __init__(self, **attrs):
        self.__dict__.update(attrs)

    def clone(self):
        return deepcopy(self)


class ConcretePrototype1(Prototype):
    def __init__(self, **attrs):
        super().__init__(**attrs)
        self.attr1 = "ConcretePrototype1"


class ConcretePrototype2(Prototype):
    def __init__(self, **attrs):
        super().__init__(**attrs)
        self.attr2 = "ConcretePrototype2"



# Создаем объекты-прототипы
p1 = ConcretePrototype1(attr3="value3")
p2 = ConcretePrototype2(attr4="value4")


# Клонируем объекты-прототипы
c1 = p1.clone()
c2 = p2.clone()


# Проверяем, что объекты-прототипы и их клоны разные
print(f"p1 is c1: {p1 is c1}")
print(f"p2 is c2: {p2 is c2}")


# Проверяем, что объекты-прототипы и их клоны имеют одинаковые значения атрибутов
print(f"p1.__dict__ == c1.__dict__: {p1.__dict__ == c1.__dict__}")
print(f"p2.__dict__ == c2.__dict__: {p2.__dict__ == c2.__dict__}")


# Проверяем, что клоны имеют те же типы, что и объекты-прототипы
print(f"type(c1) == type(p1): {type(c1) == type(p1)}")
print(f"type(c2) == type(p2): {type(c2) == type(p2)}")
