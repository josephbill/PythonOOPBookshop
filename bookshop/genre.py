class Genre:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def __str__(self) -> str:
        return f"Genre : {self.name}"