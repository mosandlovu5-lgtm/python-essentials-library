# Library Management System
# Mosa Ndlovu
# Python Essentials 1

# Returns total titles, total copies, and available copies in the whole library as tuple
def library_totals(books):
    total_titles = len(books)
    total_copies = 0
    available_copies = 0

    for book_id in books:
        total_copies += books[book_id]["total"]
        available_copies += books[book_id]["available"]

    return total_titles, total_copies, available_copies


# Returns the book id of the most borrowed book and its count, or None and 0 if no books were borrowed
def most_borrowed(books):
    if len(books) == 0:
        return None, 0

    most_borrowed_book_id = None
    most_borrowed_highest = -1

    for book_id in books:
        if books[book_id]["times_borrowed"] > most_borrowed_highest:
            most_borrowed_highest = books[book_id]["times_borrowed"]
            most_borrowed_book_id = book_id

    return most_borrowed_book_id, most_borrowed_highest

# Asks for number of copies ,and checks with try-except
def read_valid_copies():
    while True:
        try:
            copies = int(input("Number of copies: "))

            if copies >= 1:
                return copies

            print("Copies must be at least 1.")

        except ValueError:
            print("Please enter a valid whole number.")

#Adds a new book or copies to existing author
def add_book(books, next_book_number):
    title = input("Book title: ").strip()

    if title == "":
        print("Title cannot be blank.")
        return next_book_number

    author = input("Author: ").strip()

    if author == "":
        print("Author cannot be blank.")
        return next_book_number

    copies_to_add = read_valid_copies()
    if copies_to_add is None:
        return next_book_number

    # Check if the book already exists by title AND author
    for existing_book_id in books:
        existing_book = books[existing_book_id]
        if (existing_book["title"].lower() == title.lower() and
                existing_book["author"].lower() == author.lower()):
            existing_book["total"] += copies_to_add
            existing_book["available"] += copies_to_add
            print("Added " + str(copies_to_add) + " more copies of " +
                  existing_book_id + ": " + existing_book["title"] + " by " + existing_book["author"] +
                  " (now " + str(existing_book["total"]) + " total)")
            return next_book_number # Don't increment next_book_number if adding to existing

    # If not existing, create new book
    book_id = "B" + str(next_book_number)

    books[book_id] = {
        "title": title,
        "author": author,
        "total": copies_to_add,
        "available": copies_to_add,
        "times_borrowed": 0
    }

    print("Added " + book_id + ": " + title + " by " + author +
          " (" + str(copies_to_add) + " copies)")
    return next_book_number + 1


def register_member(members, next_member_number):
    name = input("Member name: ").strip()

    if name == "":
        print("Member name cannot be blank.")
        return next_member_number

    member_id = "M" + str(next_member_number)

    members[member_id] = {
        "name": name,
        "borrowed": []
    }

    print("Registered", member_id + ":", name)

    return next_member_number + 1


def borrow_book(books, members):

    member_id = input("Member ID: ").strip()

    if member_id not in members:
        print("No such member.")
        return

    book_id = input("Book ID: ").strip()

    if book_id not in books:
        print("No such book.")
        return

    if len(members[member_id]["borrowed"]) >= 3:
        print("Member has reached the borrowing limit.")
        return

    if book_id in members[member_id]["borrowed"]:
        print("Member already borrowed this book.")
        return

    if books[book_id]["available"] == 0:
        print("No copies available.")
        return

    # Borrow book
    books[book_id]["available"] -= 1
    books[book_id]["times_borrowed"] += 1

    members[member_id]["borrowed"].append(book_id)

    print(member_id + " borrowed " + book_id + ": " + books[book_id]["title"] + " by " + books[book_id]["author"] + " (" + str(books[book_id]["available"]) + " copies available)")


def return_book(books, members):
    member_id = input("Member ID: ").strip()

    if member_id not in members:
        print("No such member.")
        return

    book_id = input("Book ID: ").strip()

    if book_id not in books:
        print("No such book.")
        return

    if book_id not in members[member_id]["borrowed"]:
        print("This member does not have that book.")
        return

    members[member_id]["borrowed"].remove(book_id)
    books[book_id]["available"] += 1

    print(member_id + " returned " + book_id + ": " + books[book_id]["title"] + " by " + books[book_id]["author"])


def search_catalogue(books):
    if len(books) == 0:
        print("No books in the library.")
        return

    keyword = input("Search for: ").strip().lower()
    found = False

    for book_id in books:
        # Search by title or author
        if keyword in books[book_id]["title"].lower() or keyword in books[book_id]["author"].lower():
            book = books[book_id]

            print(
                book_id + " | " +
                book["title"] + " | " +
                book["author"] + " | Available: " +
                str(book["available"]) + "/" +
                str(book["total"])
            )
            found = True

    if not found:
        print("No books match that search.")


def member_summary(members, books):
    member_id = input("Member ID: ").strip()

    if member_id not in members:
        print("No such member.")
        return

    member = members[member_id]

    print("\nMember ID:", member_id)
    print("Name:", member["name"])
    print("Books out:", len(member["borrowed"]), "of 3 allowed")

    if len(member["borrowed"]) == 0:
        print("(no books out)")
        return

    print("Borrowed books:")
    for book_id in member["borrowed"]:
        book = books[book_id]

        print(
            "  " + book_id + ": " +
            book["title"] + " by " + book["author"]
        )


def library_report(books, members):
    if len(books) == 0:
        print("The catalogue is empty.")
        return

    total_titles, total_copies, available_copies = library_totals(books)

    copies_out = total_copies - available_copies

    most_borrowed_book_id, times = most_borrowed(books)

    print("\n===== LIBRARY REPORT =====")
    print(f"Number of titles: {total_titles}")
    print(f"Total copies: {total_copies}")
    print(f"Available copies: {available_copies}")
    print(f"Copies on loan: {copies_out}")

    if most_borrowed_book_id:
        print(
            f"Most borrowed book: {most_borrowed_book_id} - "
            f"{books[most_borrowed_book_id]['title']} by "
            f"{books[most_borrowed_book_id]['author']} "
            f"({times} times borrowed)"
        )
    else:
        print("Most borrowed book: None")

    print(f"Registered members: {len(members)}")

    at_limit = []

    for member_id in members:
        if len(members[member_id]["borrowed"]) == 3:
            at_limit.append(member_id + " " + members[member_id]["name"])

    if at_limit:
        print("Members at 3-book limit:")
        for member in at_limit:
            print("  - " + member)
    else:
        print("Members at 3-book limit: none")


# Main Program
books = {}

next_book_number = 1

members = {}
next_member_number = 1

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
       next_book_number = add_book(books, next_book_number)

    elif choice == "2":
       next_member_number = register_member(
    members,
    next_member_number
)

    elif choice == "3":
        borrow_book(books, members)

    elif choice == "4":
        return_book(books, members)

    elif choice == "5":
        search_catalogue(books)

    elif choice == "6":
        member_summary(members, books)

    elif choice == "7":
         library_report(books, members)

    elif choice == "8":
        print("Thank you for using the Library Management System Goodbye .")
        break

    else:
        print("Invalid choice. Choose 1-8.")
