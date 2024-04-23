class Book:

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages
        self.reviews = 0
        self.likes = 0
        self.circulation = 5000
        self.sold = 0


book_1984 = Book(title="1984", author="George Orwell", pages=336)
print(book_1984.__dict__)