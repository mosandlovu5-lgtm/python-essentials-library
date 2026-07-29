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

    print(member_id + " borrowed " + book_id)


    def return_book(books, members):
        member_id = input("Member ID: ").strip()

       if member_id not in members:
           print("No such member.")
           return

    book_id = input("Book ID: ").strip()

    if book_id not in members[member_id]["borrowed"]:
        print("This member does not have that book.")
        return

    members[member_id]["borrowed"].remove(book_id)
    books[book_id]["available"] += 1

     print(member_id + " returned " + book_id)



    def search_books(books):

    if len(books) == 0:
        print("No books in the library.")
        return

    keyword = input("Search for: ").strip().lower()

    found = False

    for book_id in books:

        if keyword in books[book_id]["title"].lower():

            book = books[book_id]

            print(
                book_id + " | " +
                book["title"] + " | " +
                book["author"] + " | Available: " +
                str(book["available"]) + "/" +
                str(book["total"])
            )

            found = True

    if found == False:
        print("No books match that search.")


   def member_summary(books, members):

    member_id = input("Member ID: ").strip()

    if member_id not in members:
        print("No such member.")
        return

    member = members[member_id]

    print("\nMember:", member["name"])
    print("Books out:", len(member["borrowed"]), "of 3 allowed")

    if len(member["borrowed"]) == 0:
        print("(no books out)")
        return

    for book_id in member["borrowed"]:

        book = books[book_id]

        print(
            "  " + book_id + ": " +
            book["title"]
        ) 


def library_report():
    if len(books) == 0:
        print("The catalogue is empty.")
        return

    total_titles, total_copies, available_copies = library_totals(books)

    copies_out = total_copies - available_copies

    book_id, times = most_borrowed(books)

    print("\n===== LIBRARY REPORT =====")
    print(f"Number of titles: {total_titles}")
    print(f"Total copies: {total_copies}")
    print(f"Available copies: {available_copies}")
    print(f"Copies on loan: {copies_out}")

    if book_id:
        print(
            f"Most borrowed book: {book_id} - "
            f"{books[book_id]['title']} "
            f"({times} times borrowed)"
        )

    print(f"Registered members: {len(members)}")

    at_limit = []

    for member_id in members:
        if len(members[member_id]["borrowed"]) == 3:
            at_limit.append(member_id)

    if at_limit:
        print("Members at 3-book limit:")
        for member in at_limit:
            print(member)
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
        search_books(books)

    elif choice == "6":
        member_summary(books, members)

    elif choice == "7":
         library_report(books, members)

    elif choice == "8":
        print("Thank you for using the Library Management System Goodbye .")
        break

    else:
        print("Invalid choice. Choose 1-8.")
