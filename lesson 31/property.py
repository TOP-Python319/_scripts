# property - функция, которая даёт нам возможность превращать атрибуты класса в свойства.

# property(fget=None, fset=None, fdel=None, doc=None)
# fget - функция, которая возвращает значение атрибута
# fset - функция, которая устанавливает значение атрибута
# fdel - функция, которая удаляет атрибут
# doc - документация к свойству


class Person:
    def __init__(self, name: str):
        self._name = name

    def _get_name(self):
        return self._name

    def _set_name(self, value):
        self._name = value

    def _del_name(self):
        del self._name

    name = property(
        fget=_get_name,
        fset=_set_name,
        fdel=_del_name,
        doc="Атрибут name"
    )


person = Person('Jack')
person.name
# >>>: 'Jack'
person.name = 'Mark'
person.name
# >>>: 'Mark'
del person.name
# >>>: AttributeError: 'Person' object has no attribute '_name'. Did you mean: 'name'?
