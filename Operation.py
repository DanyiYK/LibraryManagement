from datetime import datetime

class Operation:
    def __init__(self, type, book):
        self.type = type
        self.book = book
        self.date = datetime.now()
    
    def __repr__(self):
        return f"Operation(type={self.type}, book={self.book}, date={self.date})"
    
    def __eq__(self, other):
        if not isinstance(other, Operation):
            return False
        
        return self.type==other.type and self.book==other.book and self.date==other.date