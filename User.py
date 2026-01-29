from Operation import Operation
from Book import Book

MAX_BORROWED_BOOKS_PER_USER = 3

badge_number_counter = 0

class User:
    def __init__(self, name, badgeNumber=None):
        self.name = name
        self.borrowed = []
        self.operations = []

        if badgeNumber:
            self.badgeNumber = badgeNumber
        else:
            # Badge number is equal to the first 3 letters of the user name followed by a number
            global badge_number_counter
            badge_number_counter += 1

            self.badgeNumber = name[:3].lower() + str(badge_number_counter)

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        
        return self.badgeNumber==other.badgeNumber

    def __repr__(self):
        return f"User(name={self.name}, badge_number={self.badgeNumber})"
    
    def borrowBook(self, book):
        if len(self.borrowed) >= MAX_BORROWED_BOOKS_PER_USER:
            print(f"Cannot give the book: User {self} has exceeded the borrow limit of {MAX_BORROWED_BOOKS_PER_USER} books.")
            return
        
        if book.inStock <= 0:
            print(f"Book {book} is out of stock!")
            return
        
        book.inStock -= 1

        self.borrowed.append(book)
        self.operations.append(Operation("borrow", book))
        print(f"User {self} successfully borrowed book {book}")

    def returnBook(self, book):
        # Check if user has the book before doing any operation
        if book in self.borrowed:
            print(f"User {self} does not have book {book}!")
            return

        book.inStock += 1

        self.borrowed.remove(book)
        self.operations.append(Operation("return", book))

        print(f"User {self} successfully returned book {book}")