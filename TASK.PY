Ans(1):-(C)
Ans(2):-(A)
Ans(3):-(B)
Ans(4):-(B)
Ans(5):-(A)
Ans(6):-(A)
Ans(7):-(B)
Ans(8):-(C)
Ans(9):-(B)
Ans(10):-(C)
Ans(11):-(D)
Ans(12):-(A)
Ans(13):-(C)
Ans(14):-(B)
Ans(15):-(D)
Ans(16):-(C)
Ans(17):-(C)
Ans(18):-(B)
Ans(19):-(B)
Ans(20):-(B)

Q2--
ANS(1)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

print("Sum:", sum)

ANS(2)
length = 10
width = 5

area = length * width

print("Area:", area)

ANS(3)
for i in range(1, 11):
    print(i)

ANS(4)
number = 15

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

ANS(5)
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[3])


ANS(6)
def square(number):
    result = number * number
    return result

print(square(6))

ANS(7)
numbers = [10, 15, 20, 25, 30, 35]

total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print("Even Sum:", total)

ANS(8)
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

ANS(9)
marks = [80, 75, 90, 65, 70]

total = 0

for mark in marks:
    total += mark

percentage = total / len(marks) * 100

if percentage >= 35:
    result = "PASS"
else:
    result = "FAIL"

print("Total:", total)
print("Percentage:", percentage)
print("Result:", result)

ANS(10)
cart = [
    ["Keyboard", 800],
    ["Mouse", 400],
    ["USB Cable", 200]
]

total = 0

for item in cart:
    total += item[1]

if total >= 1000:
    discount = total * 10 / 100
else:
    discount = 0

final_amount = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)



Q3:-

1)--

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


book = Book(101, "Python Basics", "John Smith")

print("Book ID:", book.book_id)
print("Title:", book.title)
print("Author:", book.author)
print("Available:", book.is_available)

2)--


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    # Add a book
    def add_book(self, book):
        for b in self.books:
            if b.book_id == book.book_id:
                print("Book ID already exists!")
                return

        self.books.append(book)
        print("Book added successfully!")

    # View all books
    def view_books(self):
        if not self.books:
            print("No books available in library.")
            return

        for book in self.books:
            print("--------------------")
            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Available:", book.is_available)

    # Search book by ID
    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print("Book Found!")
                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
                print("Available:", book.is_available)
                return book

        print("Book not found!")
        return None

    # Issue a book
    def issue_book(self, book_id):
        book = self.search_book(book_id)

        if book is None:
            return

        if book.is_available:
            book.is_available = False
            print("Book issued successfully!")
        else:
            print("Book is already issued!")

    # Return a book
    def return_book(self, book_id):
        book = self.search_book(book_id)

        if book is None:
            return

        if not book.is_available:
            book.is_available = True
            print("Book returned successfully!")
        else:
            print("Book was not issued!")


# Create library object
library = Library()

# Add books
book1 = Book(101, "Python Basics", "John Smith")
book2 = Book(102, "Java Programming", "James Gosling")
book3 = Book(103, "Data Science", "Mark Taylor")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# View all books
print("\n--- All Books ---")
library.view_books()

# Issue book
print("\n--- Issue Book ---")
library.issue_book(101)

# Search book
print("\n--- Search Book ---")
library.search_book(101)

# Return book
print("\n--- Return Book ---")
library.return_book(101)

# View books again
print("\n--- Updated Book List ---")
library.view_books()


3)--


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for b in self.books:
            if b.book_id == book.book_id:
                print("Book ID already exists!")
                return

        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            print("-------------------------")
            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Available:", book.is_available)

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print("Book Found!")
                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
                print("Available:", book.is_available)
                return book

        print("Book not found!")
        return None

    def issue_book(self, book_id):
        book = self.search_book(book_id)

        if book is None:
            return

        if book.is_available:
            book.is_available = False
            print("Book issued successfully!")
        else:
            print("Book is already issued!")

    def return_book(self, book_id):
        book = self.search_book(book_id)

        if book is None:
            return

        if not book.is_available:
            book.is_available = True
            print("Book returned successfully!")
        else:
            print("Book was not issued!")


# Create library object
library = Library()

# Main menu
while True:
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        book_id = int(input("Enter Book ID to search: "))
        library.search_book(book_id)

    elif choice == "4":
        book_id = int(input("Enter Book ID to issue: "))
        library.issue_book(book_id)

    elif choice == "5":
        book_id = int(input("Enter Book ID to return: "))
        library.return_book(book_id)

    elif choice == "6":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")


4)--

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    # Add Book
    def add_book(self, book):
        for b in self.books:
            if b.book_id == book.book_id:
                print("Error: Book ID already exists!")
                return

        self.books.append(book)
        print("Book added successfully!")

    # View All Books
    def view_books(self):
        if not self.books:
            print("No books available!")
            return

        print("\n========== BOOK LIST ==========")

        for book in self.books:
            print("\nBook ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)

            if book.is_available:
                print("Status: Available")
            else:
                print("Status: Issued")

            print("------------------------------")

    # Search Book
    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print("\nBook Found!")
                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)

                if book.is_available:
                    print("Status: Available")
                else:
                    print("Status: Issued")

                return book

        print("Error: Book not found!")
        return None

    # Issue Book
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_available:
                    book.is_available = False
                    print("Book issued successfully!")
                else:
                    print("Sorry! This book is already issued.")
                return

        print("Error: Book not found!")

    # Return Book
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available:
                    book.is_available = True
                    print("Book returned successfully!")
                else:
                    print("Error: Book is not issued!")
                return

        print("Error: Book not found!")


# Create Library Object
library = Library()


# Main Menu
while True:
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        book_id = int(input("Enter Book ID: "))
        library.search_book(book_id)

    elif choice == "4":
        book_id = int(input("Enter Book ID: "))
        library.issue_book(book_id)

    elif choice == "5":
        book_id = int(input("Enter Book ID: "))
        library.return_book(book_id)

    elif choice == "6":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")


5)--


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    # Add Book
    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                print("Error: Book ID already exists!")
                return

        self.books.append(book)
        print("Book added successfully!")

    # View All Books
    def view_books(self):
        if not self.books:
            print("No books available!")
            return

        print("\n========== BOOK LIST ==========")

        for book in self.books:
            print("\nBook ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)

            if book.is_available:
                print("Status: Available")
            else:
                print("Status: Issued")

            print("------------------------------")

    # Search Book
    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print("\nBook Found!")
                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)

                if book.is_available:
                    print("Status: Available")
                else:
                    print("Status: Issued")

                return book

        print("Error: Book not found!")
        return None

    # Issue Book
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_available:
                    book.is_available = False
                    print("Book issued successfully!")
                else:
                    print("Sorry! This book is already issued.")
                return

        print("Error: Book not found!")

    # Return Book
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available:
                    book.is_available = True
                    print("Book returned successfully!")
                else:
                    print("Error: Book is not issued!")
                return

        print("Error: Book not found!")


# Main Function
def main():
    library = Library()

    while True:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            book_id = int(input("Enter Book ID: "))
            library.search_book(book_id)

        elif choice == "4":
            book_id = int(input("Enter Book ID: "))
            library.issue_book(book_id)

        elif choice == "5":
            book_id = int(input("Enter Book ID: "))
            library.return_book(book_id)

        elif choice == "6":
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


# Program Execution
if __name__ == "__main__":
    main()


6)--


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    # Add Book
    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                print("Error: Book ID already exists!")
                return

        self.books.append(book)
        print("Book added successfully!")

    # View Books
    def view_books(self):
        if not self.books:
            print("No books available!")
            return

        print("\n========== BOOK LIST ==========")

        for book in self.books:
            print("\nBook ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)

            if book.is_available:
                print("Status: Available")
            else:
                print("Status: Issued")

            print("------------------------------")

    # Search Book
    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print("\nBook Found!")
                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)

                if book.is_available:
                    print("Status: Available")
                else:
                    print("Status: Issued")

                return book

        print("Error: Book not found!")
        return None

    # Issue Book
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_available:
                    book.is_available = False
                    print("Book issued successfully!")
                else:
                    print("Sorry! This book is already issued.")
                return

        print("Error: Book not found!")

    # Return Book
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available:
                    book.is_available = True
                    print("Book returned successfully!")
                else:
                    print("Error: Book is not issued!")
                return

        print("Error: Book not found!")


# Main Function
def main():
    library = Library()

    while True:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            book_id = int(input("Enter Book ID: "))
            library.search_book(book_id)

        elif choice == "4":
            book_id = int(input("Enter Book ID: "))
            library.issue_book(book_id)

        elif choice == "5":
            book_id = int(input("Enter Book ID: "))
            library.return_book(book_id)

        elif choice == "6":
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


# Program Execution
if __name__ == "__main__":
    main()

7)--

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    # Add Book
    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                print("Error: Book ID already exists!")
                return

        self.books.append(book)
        print("Book added successfully!")

    # View All Books
    def view_books(self):
        if not self.books:
            print("No books available!")
            return

        print("\n========== BOOK LIST ==========")

        for book in self.books:
            print("\nBook ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)

            status = "Available" if book.is_available else "Issued"
            print("Status:", status)

            print("------------------------------")

    # Search Book
    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print("\nBook Found!")
                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)

                status = "Available" if book.is_available else "Issued"
                print("Status:", status)

                return book

        print("Error: Book not found!")
        return None

    # Issue Book
    def issue_book(self, book_id):
        book = self.find_book(book_id)

        if book is None:
            print("Error: Book not found!")
            return

        if book.is_available:
            book.is_available = False
            print("Book issued successfully!")
        else:
            print("Sorry! This book is already issued.")

    # Return Book
    def return_book(self, book_id):
        book = self.find_book(book_id)

        if book is None:
            print("Error: Book not found!")
            return

        if not book.is_available:
            book.is_available = True
            print("Book returned successfully!")
        else:
            print("Error: Book is not issued!")

    # Find Book (Helper Method)
    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book

        return None


# Input Validation Function
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


# Main Function
def main():
    library = Library()

    while True:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = get_integer("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            book_id = get_integer("Enter Book ID: ")
            library.search_book(book_id)

        elif choice == "4":
            book_id = get_integer("Enter Book ID: ")
            library.issue_book(book_id)

        elif choice == "5":
            book_id = get_integer("Enter Book ID: ")
            library.return_book(book_id)

        elif choice == "6":
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice! Please select 1 to 6.")


# Program Execution
if __name__ == "__main__":
    main()

































