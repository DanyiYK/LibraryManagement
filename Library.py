class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def __repr__(self):
        return f"Library(name={self.name}, catalog={self.books}, users={self.users})"

    def addBook(self, book):
        self.books.append(book)

    def addUser(self, User):
        self.users.append(User)
        
    def viewBooks(self):
        print("Registered books")
        for book in self.books:
            print(book)

    def viewUsers(self):
        print("Registered users:")
        for user in self.users:
            print(user)

    def searchBooks(self, name):
        name = name.lower()
        found_books = []

        for book in self.books:
            adjusted_title = book.title.lower()

            if adjusted_title.startswith(name):
                found_books.append(book)
        
        return found_books

    def getUserByBadgeNumber(self, badgeNumber):
        for user in self.users:
            if user.badgeId == badgeNumber:
                return user