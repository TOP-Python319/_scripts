from pprint import pprint


class Person:
    name = 'Ivan'
    age = 30


man = Person()  # в переменной man хранится экземпляр класса Person

# в экземпляре класса мы не создаём атрибуты name и age, а только ссылаемся на них в базовом классе

# у man.name такой же id как и у базового класса Person.name
print(id(Person.name))
print(id(man.name))

print(Person.__dict__)
print()
print(man.__dict__)
print()

# >>>: {'__module__': '__main__', 'name': 'Ivan', 'age': 30, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
# >>>: {}

# если изменить атрибут в ЭК, то этот атрибут с новым значением появится в словаре атрибутов __dict__
man.name = 'Petr'
print(man.__dict__)
print()
# >>>: {'name': 'Petr'}


# атрибут экземпляра класса не меняет атрибут базового класса
print('Словарь атрибутов ЭК', man.__dict__)
print('Словарь атрибутов базового класса', Person.__dict__)
# >>>: Словарь атрибутов ЭК {'name': 'Petr'}
# >>>: Словарь атрибутов базового класса {'__module__': '__main__', 'name': 'Ivan', 'age': 30, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}


# все изменения, которые мы делаем в ЭК, касаются только этих ЭК
# то есть у всех ЭК собственные пространства имён
print()
woman = Person()
woman.name = 'Olga'
print('Словарь атрибутов ЭК woman', woman.__dict__)
print('Словарь атрибутов ЭК man', man.__dict__)
print('Словарь атрибутов базового класса', Person.__dict__)
# >>>: Словарь атрибутов ЭК woman {'name': 'Olga'}
# >>>: Словарь атрибутов ЭК man {'name': 'Petr'}
# >>>: Словарь атрибутов базового класса {'__module__': '__main__', 'name': 'Ivan', 'age': 30, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}


# удалим атрибут name из экземпляра woman
# атрибут name снова будет браться из базового класса Person
# delattr(woman, 'name')
del woman.name
print()
print('Словарь атрибутов ЭК woman', woman.__dict__)
print('Словарь атрибутов ЭК man', man.__dict__)
print('Словарь атрибутов базового класса', Person.__dict__)
print(woman.name)
# >>>: Словарь атрибутов ЭК woman {}
# >>>: Словарь атрибутов ЭК man {'name': 'Petr'}
# >>>: Словарь атрибутов базового класса {'__module__': '__main__', 'name': 'Ivan', 'age': 30, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
# >>>: Ivan


# атрибут класса является общим для всех экземпляров класса
# атрибут экземпляра специфичен только для этого экземпляра