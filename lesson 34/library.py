# Создать систему управления библиотекой.
# Библиотека состоит из отделов
# (например, отдел художественной литературы, отдел научной литературы и т.д.).
# В каждом отделе есть свой набор книг.
# Книги могут перемещаться между отделами.
# Читатели могут брать книги в отделе и возвращать их обратно.

from dataclasses import dataclass


@dataclass
class Book:
    name: str
    author: str
    pages: int
    year: int
    is_available: bool = True

    def take(self):
        self.is_available = False

    def return_back(self):
        self.is_available = True


class Library:
    class Department:
        def __init__(self, name: str):
            self.name = name
            self.books = []

        def __str__(self):
            print(f'Отдел {self.name} имеет книги:')
            for book in self.books:
                print(f'{book.name} by {book.author}, status {book.is_available}')

        def add_book(self, book: Book):
            self.books.append(book)

        def del_book(self, book: Book):
            self.books.remove(book)

    def __init__(self, name: str):
        self.name = name
        self.departments = {}

    def __str__(self):
        print(f'Библиотека {self.name} имеет отделы:')
        for department in self.departments:
            for book in self.departments[department].books:
                print(f'{book.name} by {book.author}, status {book.is_available}')

    def add_department(self, name: str):
        self.departments[name] = self.__class__.Department(name)

    def move_book(self,
                  book: Book,
                  department_from: Department,
                  department_to: Department):
        department_from.del_book(book)
        department_to.add_book(book)


library = Library('Ленинская библиотека')
FICTION_BOOKS = 'Художественная литература'
SCIENCE_BOOKS = 'Научная литература'
library.add_department(FICTION_BOOKS)
library.add_department(SCIENCE_BOOKS)

brave_new_world = Book('Brave New World', 'Aldous Huxley', 311, 1932)
anna_karenina = Book('Anna Karenina', 'Leo Tolstoy', 864, 1877)
fight_club = Book('Fight Club', 'Chuck Palahniuk', 366, 1996)
universe_in_a_nutshell = Book('Universe in a nutshell', 'Stephen Hawking', 480, 1976)

library.departments[FICTION_BOOKS].add_book(brave_new_world)
library.departments[FICTION_BOOKS].add_book(anna_karenina)
library.departments[FICTION_BOOKS].add_book(fight_club)
library.departments[FICTION_BOOKS].add_book(universe_in_a_nutshell)

library.move_book(universe_in_a_nutshell, library.departments[FICTION_BOOKS], library.departments[SCIENCE_BOOKS])

print(library)
