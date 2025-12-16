class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.book_id} - {self.title} - {self.author} - {status}"

