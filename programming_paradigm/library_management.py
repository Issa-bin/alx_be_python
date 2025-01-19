class Book:
    def __init__(self, title,author):
        self.title = title
        self.author = author
        self.is_available = True

    def __sr__(self):
        return f"{self.title}by {self.author}"
    
class Library:
    def __init__(self):
        self.books =[]

    def add_book(self,book):
        self.books.append(book)

    def list_available_books(self):
        for book in self.books:
            if book.is_available:
                print(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                return
            print(f"Sorry, the book '{title}' is not available.")

    def return_book(self,title):
        for book in self.books:
            if book.title == title and not book.is_available:
                book.is_available = True
                return
            print("Sorry, there is no book '{title}' checked out.")
