from logging import exception


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.transactions = []
    #Add book
    def add_book(self, book):
        self.books[book.book_id] = book
    #Register member
    def register_member(self, member):
        self.members[member.member_id] = member
    #Borrow Book
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            raise exception("Member not found")
        if book_id not in self.books:
            raise exception("Book not found")
        book = self.books[book_id]
        member = self.members[member_id]
        if not book.is_available:
            raise exception("Book already borrowed")
        book.is_available = False
        member.borrowed_books.append(book)
        print(f"member {member.first_name} borrowed book {book.title}")
    #Return book
    def return_book(self, book_id, member_id):
        member = self.members[member_id]
        book = self.books[book_id]
        if book not in member.borrowed_books:
            raise exception("This book was not borrowed by member")
        book.is_available = True
        member.borrowed_books.remove(book)
        for t in self.transactions:
            if t.book == book and t.return_date is None:
                t.return_book()
        print(f"member {member.first_name} returned book {book.title}")
    #Show books
    def show_books(self):
        for book in self.books.values():
            print(book)
