class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Information about book: {self.title}, {self.author}"


class Library:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        return self.books[index]
