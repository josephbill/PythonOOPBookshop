import sys
import os
# Adjust the path to the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from bookshop.author import Author 
from bookshop.genre import Genre
from bookshop.book import Book 


# create instances of my classes 
# author1 = Author("Joseph")
genre1 = Genre("Thriller")
# book1 = Book("Book One", genre1,author1)
# print(author1)
# print(genre1)
# print(book1)

author2 = Author("Mary")
author2.write_book("Another Book", genre1)
author2.write_book("Another Book 2", genre1)
print(author2)