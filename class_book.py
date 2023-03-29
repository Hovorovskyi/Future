class Book:

    def __init__(self, name, autor, pages):
        self.name = name
        self.autor = autor
        self.pages = pages

    def __repr__(self):
        return f"({self.name}, {self.autor}, {self.pages})"

    def __str__(self):
        return f"Name: {self.name}.\nAutor: {self.autor}.\nPages: {self.pages}."

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.autor == other.autor and self.name == other.name

    def __lt__(self, other):
        return self.pages < other.pages


if __name__ == '__main__':
    book1 = Book('Hard to be a God', 'Strugatsky`s brothers', 360)
    book2 = Book('West front', 'Remark', 350)
    book3 = Book('American tragedy', 'Draizer', 940)
    book4 = Book('Sister Kerry', 'Draiaer', 380)

    books = [book1, book2, book3]

    for i in books:
        print(i)
        print(len(i))

    print(book2 == book1)

    if book4 in books:
        print('It`s in')
    else:
        print('Book not in list')

    print(max(books))
    print(min(books))
    print(sorted(books))
