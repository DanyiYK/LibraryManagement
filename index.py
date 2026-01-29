from Library import Library
from User import User
from Book import Book
from Author import Author
from Action import Action

new_library = Library("Libreria di Pescara")

def printActions(action_list):
    print("Actions:")
    
    for i, v in enumerate(action_list):
        print(f"  {i + 1}. {v.desc}")

def sendContinueMessage():
    input("Press enter to continue...")

def promptAddUser():
    name = input("Insert User's name: ")
    
    if name=="":
        print("User name cannot be empty!")
    else:
        new_user = User(name.strip())

def promptAddBook():
    name = input("Insert Book's name: ")
    isbn = input("Insert Book's ISBN: ")
    author_name = input("Insert Author's name: ")
    author_nationality = input("Insert Author's nationality: ")

    try:
        book_count = int(input("Insert book count: "))
    except:
        book_count = 1

    new_author = Author(author_name, author_nationality)
    new_book = Book(name, bookISBN, new_author, book_count)

    print("The book was sucessfully added!")

def showUsers():
    new_library.viewUsers()

def showBooks():
    new_library.viewBooks()

def searchBooks():
    name = input("Search book: ")
    found = new_library.searchBooks(name)

    print("Here's the result for your query:")
    
    if len(found)==0:
        print("No books were found :(")
        return

    for i, book in enumerate(found):
        print(f"  {i + 1}. {book}")

def promptBorrowBook():
    badgeId = input("Insert User's Badge ID: ")
    user:User = new_library.getUserByBadgeNumber(badgeId)

    if not user:
        print(f"There's no user with such Badge ID: {badgeId}!")
        return

    bookISBN = input("Insert book's ISBN:")
    book = new_library.getBookByISBN(bookISBN)

    if not book:
        print(f"There's no book with such ISBN: {bookISBN}!")
        return
    
    user.borrowBook(book)
    

def promptReturnBook():
    pass

def showUserOperations():
    pass

def closeProgram():
    global running
    running = False

ACTIONS = [
    Action("Add user", promptAddUser),
    Action("Add book", promptAddBook),
    Action("Show all users", showUsers),
    Action("Show all books", showBooks),
    Action("Search books", searchBooks),
    Action("Borrow a book", promptBorrowBook),
    Action("Return a book", promptReturnBook),
    Action("Show user operations", showUserOperations),
    Action("Exit the program", closeProgram),
]


while True:
    printActions(ACTIONS)

    try:
        selected_action = int(input("Select action: "))
    except ValueError:
        print("Please, input a real number!")

        continue
    
    if selected_action <= 1 or selected_action > len(ACTIONS):
        print(f"The action id must be between 0 and {len(ACTIONS)}!")
    
    ACTIONS[selected_action].fun()

    sendContinueMessage()