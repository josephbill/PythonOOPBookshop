class Book: 
    def __init__(self, title,genre,author):
        self.title = title
        self.genre = genre
        self.author = author

    def __str__(self) -> str:
        return f"Book : {self.title} , Author: {self.author.name} , Genre: {self.genre.name}"
        