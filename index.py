from Library import Library
from User import User
from Book import Book
from Author import Author

new_library = Library("Libreria di Pescara")

test_user = User("Giancarlo")

test_author = Author("Lev Tolstoj", "RU")
test_book = Book("Guerra e pace", "ABCDEFG", test_author, 3)

test_user.borrowBook(test_book)