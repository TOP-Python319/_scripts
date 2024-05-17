# class object:
#     """
#     The base class of the class hierarchy.

#     When called, it accepts no arguments and returns a new featureless
#     instance that has no instance attributes and cannot be given any.
#     """
from pprint import pprint


class Person:  # на самом деле это Person(object)
    ...


class Doctor(Person):
    ...


class Architect(Person):
    ...


class Teacher(Person):
    ...


print(issubclass(Person, object))
print(issubclass(Doctor, object))
print(issubclass(Architect, object))

pprint(dir(object))
# [   
#     '__class__',
#     '__delattr__',
#     '__dir__',
#     '__doc__',
#     '__eq__',
#     '__format__',
#     '__ge__',
#     '__getattribute__',
#     '__gt__',
#     '__hash__',
#     '__init__',
#     '__init_subclass__',
#     '__le__',
#     '__lt__',
#     '__ne__',
#     '__new__',
#     '__reduce__',
#     '__reduce_ex__',
#     '__repr__',
#     '__setattr__',
#     '__sizeof__',
#     '__str__',
#     '__subclasshook__'
# ]

obj1 = object()
obj2 = object()
print(obj1 == obj1)
print(obj1 == obj2)

pprint(dir(Person))
# [   
#     '__class__',
#     '__delattr__',
#     '__dir__',
#     '__doc__',
#     '__eq__',
#     '__format__',
#     '__ge__',
#     '__getattribute__',
#     '__gt__',
#     '__hash__',
#     '__init__',
#     '__init_subclass__',
#     '__le__',
#     '__lt__',
#     '__ne__',
#     '__new__',
#     '__reduce__',
#     '__reduce_ex__',
#     '__repr__',
#     '__setattr__',
#     '__sizeof__',
#     '__str__',
#     '__subclasshook__'
# ]
p1 = Person()
p2 = Person()
print(p1 == p1)
print(p1 == p2)
