print("Contact book ")
contacts = {}
while True:
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")
    elif choice == "2":
        if contacts:
            for name, phone in contacts.items():
                print(name, "-", phone)
        else:
            print("No contacts found.")
    elif choice == "3":
        name = input("Enter contact name to search: ")
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")
    elif choice == "4":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
