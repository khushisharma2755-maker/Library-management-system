
import json
import os

# ----------------- Book Class -----------------
class Book:
    def _init_(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["isbn"], data["available"])

# ----------------- Library class -----------------
class Library:
    def _init_(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    data = json.load(f)
                    self.books = [Book.from_dict(book) for book in data]
                except json.JSONDecodeError:
                    self.books = []
        else:
            self.books = []

    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save_books()
        print(f"Book '{title}' added successfully.")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    self.save_books()
                    print(f"You borrowed '{book.title}'.")
                else:
                    print("Book is already borrowed.")
                return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    self.save_books()
                    print(f"You returned '{book.title}'.")
                else:
                    print("This book was not borrowed.")
                return
        print("Book not found.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                status = "Available" if book.available else "Borrowed"
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")

# ----------------- Main Program -----------------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add New Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. List All Books")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)

        elif choice == "2":
            isbn = input("Enter ISBN of book to borrow: ")
            library.borrow_book(isbn)

        elif choice == "3":
            isbn = input("Enter ISBN of book to return: ")
            library.return_book(isbn)

        elif choice == "4":
            library.list_books()

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
