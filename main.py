from system.library import Library
from system.member import Member
from system.book import Book

if __name__ == "__main__":
    library = Library()


    # Add books
    library.add_book(Book(1, "Clean Code", "Robert Martin"))
    library.add_book(Book(2, "Python Crash Course", "Eric"))

    # Register members
    library.register_member(Member(101, "Sneha"))
    library.register_member(Member(102, "Rahul"))

    # Borrow & Return
    library.borrow_book(101, 1)
    library.borrow_book(102, 2)

    library.show_books()

    library.return_book(1, 101)

    library.show_books()
