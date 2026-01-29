badge_number_counter = 0

class User:
    def __init__(self, name, badgeNumber=None):
        self.name = name
        badge_number_counter += 1

        if badgeNumber:
            self.badge_number = badgeNumber
        else:
            # Badge number is equal to the first 3 letters of the user name followed by a number
            self.badge_number = name[:3].lower() + badge_number_counter

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        
        return self.badge_number==other.badge_number

    def __repr__(self):
        return f"name={self.name}, badge_number={self.badge_number}"
    
    def borrowBook(self, book):
        pass

    def returnBook(self, book):
        pass