# Абстрактный класс является абстракцией того, что должны делать его наследники, но не определяет, как именно это должно быть сделано.
# Абстрактный класс не может иметь собственных ЭК

# Абстрактный метод - это метод, который не объявлен в абстратном классе, но не имеет реализации. По сути - шаблон для метода в дочерних классах.


from abc import ABC, abstractmethod


# базовый вид абстрактного класса
# class Class(ABC):
#     @abstractmethod
#     def method(self):
#         pass