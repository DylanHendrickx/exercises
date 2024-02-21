class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for boek in self.books:
            if book.title == boek.title and book.author == boek.author:
                self.books.remove(boek)

    def search_books(self, search_string):
        search_list = []
        for book in self.books:
             if (
                search_string.lower() in book.title.lower()
                or search_string.lower() in book.author.lower()
            ):
                 search_list.append(book)
        return search_list

