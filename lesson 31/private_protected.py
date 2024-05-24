# публичные атрибуты

# class Book:
#     def __init__(self, title, author) -> None:
#         self.title = title
#         self.author = author


# защищённые атрибуты
# работает на уровне договорённости

# class Book:
#     def __init__(self, title, author) -> None:
#         self._title = title
#         self._author = author


# b = Book("War and Peace", "Leo Tolstoy")
# print(b._title)
# b._title = "Anna Karenina"
# print(b._title)


# приватные атрибуты

class Book:
    def __init__(self, title, author) -> None:
        self.__title = title
        self.__author = author


b = Book("War and Peace", "Leo Tolstoy")
# print(b.__title)
# AttributeError: 'Book' object has no attribute '__title'

print(dir(b))
# ['_Book__author', '_Book__title', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# print(b._Book__title)


# class Person:
#     def __init__(self, name, age, eye_color, hair_color, weight, height) -> None:
#         self.name = name
#         self.age = age
#         self.eye_color = eye_color
#         self.hair_color = hair_color
#         self.weight = weight
#         self.height = height

#     def set_eye_color(self, eye_color):
#         self.eye_color = eye_color
#         print(self.eye_color)

#     def calc_salary(self):
#         pass

#     def years_remaining(self):
#         pass

#     def years_until_retirement(self):
#         pass
