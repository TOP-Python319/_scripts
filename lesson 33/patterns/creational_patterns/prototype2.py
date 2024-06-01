from copy import deepcopy


class EnemyPrototype:
    def __init__(self, **attrs):
        self.__dict__.update(attrs)

    def clone(self):
        return deepcopy(self)


class ConcreteEnemy1(EnemyPrototype):
    def __init__(self, **attrs):
        super().__init__(**attrs)
        self.name = "ConcreteEnemy1"
        self.health = 100
        self.speed = 5
        self.damage = 20


class ConcreteEnemy2(EnemyPrototype):
    def __init__(self, **attrs):
        super().__init__(**attrs)
        self.name = "ConcreteEnemy2"
        self.health = 200
        self.speed = 3
        self.damage = 30


class EnemyFactory:
    def __init__(self):
        self.prototypes = {
            "ConcreteEnemy1": ConcreteEnemy1(),
            "ConcreteEnemy2": ConcreteEnemy2(),
        }

    def create_enemy(self, name, **attrs):
        prototype = self.prototypes[name]
        enemy = prototype.clone()
        enemy.__dict__.update(attrs)
        return enemy


# Создаем фабрику врагов
factory = EnemyFactory()

# Создаем врагов с помощью фабрики
e1 = factory.create_enemy("ConcreteEnemy1", position=(10, 20))
e2 = factory.create_enemy("ConcreteEnemy2", position=(30, 40))

# Проверяем, что враги имеют ожидаемые значения атрибутов
print(f"e1.__dict__: {e1.__dict__}")
print(f"e2.__dict__: {e2.__dict__}")
