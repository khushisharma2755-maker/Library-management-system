# Library-management-system

This is a simple library management system written in Python. The system allows you to add books, borrow books, return books, and list all books.

# Approach
The system uses object-oriented programming to define two classes: Book and Library. The Book class represents a book with attributes such as title, author, ISBN, and availability. The Library class represents a library with methods to add, borrow, return, and list books.

# How to Run
1. Save the code in a file named library_management_system.py.
2. Open a terminal or command prompt and navigate to the directory where the file is saved.
3. Run the program using the command python library_management_system.py.

# Example Input/Output
Adding a Book
Enter choice: 1
Enter title: Python Programming
Enter author: John Doe
Enter ISBN: 1234567890
Book 'Python Programming' added successfully.

Borrowing a Book
Enter choice: 2
Enter ISBN of book to borrow: 1234567890
You borrowed 'Python Programming'.

Returning a Book
Enter choice: 3
Enter ISBN of book to return: 1234567890
You returned 'Python Programming'.

Listing All Books
Enter choice: 4
Title: Python Programming, Author: John Doe, ISBN: 1234567890, Status: Available

# Challenges Faced
1. Data Persistence: One of the challenges faced was implementing data persistence using a JSON file. This required careful consideration of how to serialize and deserialize book objects.
2. Error Handling: Another challenge was handling errors that may occur during file operations or user input. This required implementing try-except blocks to catch and handle exceptions.
3. User Experience: Designing a user-friendly interface was also a challenge. This required careful consideration of how to present menu options and handle user input.
