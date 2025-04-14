class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Default to available

    def borrow(self):
        if self.available:
            self.available = False
            print(f'📖 You borrowed "{self.title}".')
        else:
            print(f'❌ "{self.title}" is already borrowed.')

    def return_book(self):
        self.available = True
        print(f'✅ "{self.title}" has been returned.')

# Example Usage
book1 = Book("Python Basics", "John Doe")
book2 = Book("OOP in Python", "Jane Smith")

book1.borrow()  
book1.return_book()  
