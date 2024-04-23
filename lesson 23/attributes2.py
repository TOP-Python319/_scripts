# getattr(), hasattr(), setattr(), delattr()


# обращение к атрибутам возможно через точку

class Person:
    name = 'Alex'
    age = 25


print(Person.name)
print(Person.age)


# удобно тем что IDE подсказывает названия атрибутов
# обращаться через точку можно только к существующим атрибутам
# print(Person.salary)  # выдаст ошибку AttributeError


# getattr()
# можно использовать функцию getattr()
# возвращает значение именованного атрибута объекта, если атрибут не найден,
# то возвращает значение по умолчанию

# getattr(object, name[, default])
# object - объект, в котором будет осуществлён поиск
# name - название атрибута
# не обязательный аргумент default - значение по умолчанию, если атрибут не найден
print('###############')
print('getattr() работает так: ')
print(getattr(Person, 'name', 'default_name'))
print(getattr(Person, 'salary', 'default_salary'))
print()
print('Person после getattr: ', Person.__dict__)
print()


# hasattr()
# проверяет наличие атрибута у объекта
# возвращает True или False

# hasattr(object, name)
# object - объект, в котором будет осуществлён поиск
# name - название атрибута
print('###############')
print('hasattr() работает так: ')
print(hasattr(Person, 'name'))
print(hasattr(Person, 'salary'))


# setattr()
# устанавливает или изменяет значение атрибута объекта
# setattr(object, name, value)
# object - объект, в котором будет осуществлён поиск
# name - название атрибута
# value - значение атрибута
print('###############')
setattr(Person, 'salary', 1000)
print(Person.salary)
print()
print('Person после setattr: ', Person.__dict__)
print()
setattr(Person, 'name', 'Alexey')
print(Person.name)


# {'Georgia': 'Tbilisi', 'Russia': 'Moscow', 'Ukraine': 'Kiev', 'Uzbekistan': 'Tashkent'}
# class Country:
#     georgia = 'Tbilisi'
#     russia = 'Moscow'
#     ukraine = 'Kiev'
#     # uzbekistan = 'Tashkent' 

# Country.'uzbekistan' = 'Tashkent'
# setattr(Country, 'uzbekistan', 'Tashkent')


# delattr()
# удаляет атрибут из объекта
# delattr(object, name)
# object - объект, в котором будет осуществлён поиск
# name - название атрибута
print('###############')
delattr(Person, 'salary')
# print(Person.salary)  # AttributeError: type object 'Person' has no attribute 'salary'
print()
print('Person после delattr: ', Person.__dict__)
print()
delattr(Person, 'name')
# delattr(Person, 'name')  # нельзя удалить несуществующий атрибут AttributeError: name
# print(Person.name)  # AttributeError: type object 'Person' has no attribute 'name'


# delattr часто используется вместе с hasattr
if hasattr(Person, 'name'):  # возвращает False
    delattr(Person, 'name')  # => не попытается удалить атрибут и не выдаст ошибку