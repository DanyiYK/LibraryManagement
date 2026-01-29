class Book:
    def __init__(self, title, isbn, author, count=1):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.count = count
        self.inStock = count

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        
        return self.isbn
    
    def __repr__(self):
        return f"Book(title={self.title}, isbn={self.isbn}, author={self.author}, count={self.count}, inStock={self.inStock})"