class Book:
    title = 'Анна Каренина'
    author = 'Лев Толстой'
    genre = 'роман'
    pages = 1225


print(f'Автор: {Book.author}, Книга: {Book.title}')
print(getattr(Book, 'color', 'black'))
print(getattr(Book, 'pages'))

print(Book.__dict__)

setattr(Book, 'pages', 1000)

if hasattr(Book, 'genre'):
    delattr(Book, 'genre')

print(Book.__dict__)

setattr(Book, 'genre', 'детектив')

print(Book.__dict__)
