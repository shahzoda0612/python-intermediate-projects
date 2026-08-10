print("Inventory management system ")
inventory = {}
while True:
    print("1. Add product")
    print("2. View products")
    print("3. Search product")
    print("4. Add stock")
    print("5. Remove stock")
    print("6. Delete product")
    print("7. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter product name: ")
        if name in inventory:
            print("Product already exists.")
        else:
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            inventory[name] = {
                "price": price,
                "quantity": quantity
            }
            print("Product added successfully!")
    elif choice == "2":
        if inventory:
            for name, product in inventory.items():
                print(
                    name,
                    "- Price:",
                    product["price"],
                    "- Quantity:",
                    product["quantity"]
                )
        else:
            print("No products found.")
    elif choice == "3":
        name = input("Enter product name to search: ")
        if name in inventory:
            product = inventory[name]
            print("Product:", name)
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])
        else:
            print("Product not found.")
    elif choice == "4":
        name = input("Enter product name: ")
        if name in inventory:
            quantity = int(input("Enter quantity to add: "))
            if quantity > 0:
                inventory[name]["quantity"] += quantity
                print("Stock added successfully!")
            else:
                print("Quantity must be greater than 0.")
        else:
            print("Product not found.")
    elif choice == "5":
        name = input("Enter product name: ")
        if name in inventory:
            quantity = int(input("Enter quantity to remove: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
            elif quantity > inventory[name]["quantity"]:
                print("Not enough stock.")
            else:
                inventory[name]["quantity"] -= quantity
                print("Stock removed successfully!")
        else:
            print("Product not found.")
    elif choice == "6":
        name = input("Enter product name to delete: ")
        if name in inventory:
            del inventory[name]
            print("Product deleted successfully!")
        else:
            print("Product not found.")
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
