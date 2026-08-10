print(" Library management system")
books = []
while True:
    print("1. Add book")
    print("2. View books")
    print("3. Search book")
    print("4. Borrow book")
    print("5. Return book")
    print("6. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        book = {
            "title": title,
            "author": author,
            "available": True
        }
        books.append(book)
        print("Book added successfully!")
    elif choice == "2":
        if books:
            for book in books:
                status = "Available" if book["available"] else "Borrowed"
                print(
                    book["title"],
                    "-",
                    book["author"],
                    "-",
                    status
                )
        else:
            print("No books found.")
    elif choice == "3":
        title = input("Enter book title to search: ")
        found = False
        for book in books:
            if book["title"].lower() == title.lower():
                status = "Available" if book["available"] else "Borrowed"
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Status:", status)
                found = True
                break
        if not found:
            print("Book not found.")
    elif choice == "4":
        title = input("Enter book title to borrow: ")
        found = False
        for book in books:
            if book["title"].lower() == title.lower():
                found = True
                if book["available"]:
                    book["available"] = False
                    print("Book borrowed successfully!")
                else:
                    print("Book is already borrowed.")
                break
        if not found:
            print("Book not found.")
    elif choice == "5":
        title = input("Enter book title to return: ")
        found = False
        for book in books:
            if book["title"].lower() == title.lower():
                found = True
                if not book["available"]:
                    book["available"] = True
                    print("Book returned successfully!")
                else:
                    print("This book was not borrowed.")
                break
        if not found:
            print("Book not found.")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

