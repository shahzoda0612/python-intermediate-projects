print("Expense tracker ")
expenses = []
while True:
    print("1. Add expense")
    print("2. View expenses")
    print("3. Total expenses")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        expense = {
            "name": name,
            "amount": amount
        }
        expenses.append(expense)
        print("Expense added successfully!")
    elif choice == "2":
        if expenses:
            for expense in expenses:
                print(
                    expense["name"],
                    "-",
                    expense["amount"]
                )
        else:
            print("No expenses found.")
    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense["amount"]
        print("Total expenses:", total)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")