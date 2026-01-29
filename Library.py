import User
import Book

class Library:
    def __init__(self, name):
        self.name = name
        self.catalog = []
        self.users = []

    def __repr__(self):
        return f"Library(name={self.name}, catalog={self.catalog}, users={self.users})"

    def addBook(self, name, isbn, author, count=1):
        pass

    def addUser(self, name):
        pass

    def viewBooks(self):
        pass

    def viewUsers(self):
        pass

    def searchBooks(self, name):
        pass

    def getUserByBadgeId(self, badgeId):
        pass