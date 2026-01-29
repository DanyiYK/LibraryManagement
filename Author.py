class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
    
    def __repr__(self):
        return f"Author(name={self.name}, nationality={self.nationality})"
    
    def __eq__(self, other):
        if not isinstance(other, Author):
            return False
        
        return self.name==other.name and self.nationality and other.nationality