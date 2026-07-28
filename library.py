# Library Management System
# Mosa Ndlovu
# Python Essentials 1
def libray_totals():
    print("libray tools - Coming soon")


def most_borrowed():
    print("Most borrowed - Coming Soon")


def read_valid_copies():
    print("Valid Copies - Coming Soon")

        
def add_book():
    title = input("Book title: ").strip()

    if title == "":
        print("Title cannot be blank.")
        return next_book_number

    author = input("Author: ").strip()

    if author == "":
        print("Author cannot be blank.")
        return next_book_number

    copies = read_valid_copies()

    book_id = "B" + str(next_book_number)

    books[book_id] = {
        "title": title,
        "author": author,
        "total": copies,
        "available": copies,
        "times_borrowed": 0
    }

    print("Added", book_id + ":", title)

    return next_book_number + 1


def register_member():
    print("Register Member - Coming Soon")


def borrow_book():
    print("Borrow Book - Coming Soon")


def return_book():
    print("Return Book - Coming Soon")


def search_books():
    print("Search Books - Coming Soon")


def member_summary():
    print("Member Summary - Coming Soon")


def library_report():
    print("Library Report - Coming Soon")


# Main Program
books = {}

next_book_number = 1

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Books")
    print("6. Member Summary")
    print("7. Library Report")
    print("8. Exit")

    choice = input("Choose an option: ").strip()
    

    if choice == "1":
        add_book()

    elif choice == "2":
        register_member()

    elif choice == "3":
        borrow_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        search_books()

    elif choice == "6":
        member_summary()

    elif choice == "7":
        library_report()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
