from abc import ABC, abstractmethod


# Интерфейс, который должен быть реализован
class IComponent(ABC):
    @abstractmethod
    def operation(self):
        pass


# Конкретная реализация интерфейса IComponent для листовых объектов
class Leaf(IComponent):
    def operation(self):
        print("Leaf: Operation")


# Базовый класс-композит, реализующий интерфейс IComponent и содержащий список дочерних объектов-компонентов
class Composite(IComponent):
    def __init__(self):
        self._components = []

    def operation(self):
        for component in self._components:
            component.operation()

    def add(self, component: IComponent):
        self._components.append(component)

    def remove(self, component: IComponent):
        self._components.remove(component)

    def get_child(self, index: int):
        return self._components[index]


# Конкретная реализация интерфейса IComponent для объектов-композитов
class ConcreteComposite(Composite):
    def operation(self):
        print("ConcreteComposite: Operation")
        super().operation()


# Пример использования
if __name__ == "__main__":
    leaf_1 = Leaf()
    leaf_2 = Leaf()
    composite_1 = ConcreteComposite()
    composite_2 = ConcreteComposite()
    composite_1.add(leaf_1)
    composite_1.add(composite_2)
    composite_2.add(leaf_2)
    composite_1.operation()
