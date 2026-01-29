from Operation import Operation
from Book import Book

MAX_BORROWED_BOOKS_PER_USER = 3

badge_number_counter = 0

class User:
    def __init__(self, name, badgeNumber=None):
        self.name = name
        self.borrowed = []
        self.operations = []

        badge_number_counter += 1

        if badgeNumber:
            self.badgeNumber = badgeNumber
        else:
            # Badge number is equal to the first 3 letters of the user name followed by a number
            self.badgeNumber = name[:3].lower() + badge_number_counter

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        
        return self.badgeNumber==other.badgeNumber

    def __repr__(self):
        return f"name={self.name}, badge_number={self.badge_number}"
    
    def borrowBook(self, book):
        if len(self.borrowed) >= MAX_BORROWED_BOOKS_PER_USER:
            return
        
        if not book.inStock <= 0:
            return
        
        book.inStock -= 1

        self.borrowed.append(book)
        self.operations.append(Operation("borrow", book))


    def returnBook(self, book):
        pass