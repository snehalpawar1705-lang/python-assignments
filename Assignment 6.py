class Library:
    
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True

    def check_out(self):
        if self.available:
            self.available = False
            print(self.book_name, "by", self.author, "has been checked out.")
        else:
            print(self.book_name, "is currently unavailable.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(self.book_name, "has been returned.")
        else:
            print(self.book_name, "was not checked out.")

    def display_status(self):
        if self.available:
            print(self.book_name, "by", self.author, "- Available")
        else:
            print(self.book_name, "by", self.author, "- Checked Out")


# Creating objects
book1 = Library("Python Programming", "John Smith")
book2 = Library("Data Structures", "Mark Allen")

# Display status
book1.display_status()
book2.display_status()

# Checkout book
book1.check_out()

# Display again
book1.display_status()

# Return book
book1.return_book()

# Display again
book1.display_status()
