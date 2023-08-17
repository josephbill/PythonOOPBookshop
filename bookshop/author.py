# from bookshop import Book 
from bookshop.book import Book


class Author:
    def __init__(self, name):
        self.name = name 
        self.books = []

    def write_book(self, title, genre):
         book = Book(title,genre,self)
         self.books.append(book)
         genre.add_books(book) 
         return book
    
    def __str__(self) -> str:
        book_details = "\n".join(str(book) for book in self.books)
        return f"Author: {self.name} ,\n Books: \n{book_details}"