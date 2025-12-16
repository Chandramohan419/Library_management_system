'''from datetime import datetime
class Transaction:
    def __init__(self, book, title, author, created_at, member):
        self.book_id = book
        self.title = title
        self.author = author
        self.created_at = created_at
        self.member = member
    def return_book(self):
        self.return_book() = datetime.now()'''


from datetime import datetime

class Transaction:
    def __init__(self, member, book):
        self.member = member
        self.book = book
        self.borrow_date = datetime.now()
        self.return_date = None

    def return_book(self):
        self.return_date = datetime.now()

