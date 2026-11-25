# Library Management System
A simple Library Management System built using Python and Object-Oriented Programming (OOP) concepts. The project allows librarians to manage books, register members, borrow books, and return books.

# Features
Book Management:
Add new books to the library
View available books
Track borrowed books

Member Management:
Register new members
Store member information
Track member borrowing activity

Borrowing System:
Borrow available books
Prevent borrowing of unavailable books
Record borrowing transactions

Return System:
Return borrowed books
Update availability status
Maintain accurate inventory
# Project Structure
library_management/
│
├── system/
│   ├── book.py
│   ├── member.py
│   └── library.py
│   └── transaction.py
│   └── init.py
│
├── main.py
├── README.md
└── requirements.txt
# Classes Used
Book
Represents a library book.

Attributes:

Book ID
Title
Author
Availability Status

Example:
Book(1, "Clean Code", "Robert Martin")

# Member
Represents a library member.
Attributes:
Member ID
Member Name
Borrowed Books
Example:
Member(101, "Sneha")

# Library
Responsible for:
Adding books
Registering members
Borrowing books
Returning books
Displaying library inventory

# Workflow
Add Books
    ↓
Register Members
    ↓
Borrow Books
    ↓
Update Availability
    ↓
Return Books
    ↓
Display Status

# Sample Usage
library = Library()

library.add_book(Book(1, "Clean Code", "Robert Martin"))
library.add_book(Book(2, "Python Crash Course", "Eric"))

library.register_member(Member(101, "Sneha"))
library.register_member(Member(102, "Rahul"))

library.borrow_book(101, 1)
library.borrow_book(102, 2)

library.show_books()

library.return_book(1, 101)

library.show_books()
# Sample Output
Book added successfully
Member registered successfully

Book 'Clean Code' borrowed by Sneha
Book 'Python Crash Course' borrowed by Rahul

Available Books:
Book ID: 1 | Clean Code | Borrowed
Book ID: 2 | Python Crash Course | Borrowed

Book returned successfully

Available Books:
Book ID: 1 | Clean Code | Available
Book ID: 2 | Python Crash Course | Borrowed
# OOP Concepts Demonstrated
Encapsulation:
Book data is stored within Book objects.
Member information is stored within Member objects.

Composition:
Library contains collections of Books and Members.

Abstraction:
Library methods hide implementation details from users.
Object-Oriented Design
Library
 ├── Books
 └── Members
 
# Key Learning Outcomes
Python Classes and Objects
Data Structures (Lists and Dictionaries)
Object-Oriented Programming
Method Design
Modular Programming
Real-World System Modeling
Future Enhancements
# Version 2
Book Search Functionality
ISBN Support
Borrowing Due Dates
Late Return Tracking
# Version 3
SQLite Database Integration
User Authentication
Admin Dashboard
Reservation System
# Version 4
REST APIs using FastAPI
Docker Deployment
Email Notifications
Web-Based Interface
# Technologies Used
Python 3.x
Object-Oriented Programming (OOP)
Standard Python Libraries
# Author
Chandramohan Pokuru
Library Management System built using Python and Object-Oriented Programming principles.
