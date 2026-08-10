print("Banking system ")
accounts = {}
while True:
    print("1. Create account")
    print("2. View balance")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Transfer money")
    print("6. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter your name: ")
        if name in accounts:
            print("Account already exists.")
        else:
            accounts[name] = 0.0
            print("Account created successfully!")
    elif choice == "2":
        name = input("Enter your name: ")
        if name in accounts:
            print("Your balance:", accounts[name])
        else:
            print("Account not found.")
    elif choice == "3":
        name = input("Enter your name: ")
        if name in accounts:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                accounts[name] += amount
                print("Money deposited successfully!")
                print("Your balance:", accounts[name])
            else:
                print("Amount must be greater than 0.")
        else:
            print("Account not found.")
    elif choice == "4":
        name = input("Enter your name: ")
        if name in accounts:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            elif amount > accounts[name]:
                print("Insufficient balance.")
            else:
                accounts[name] -= amount
                print("Money withdrawn successfully!")
                print("Your balance:", accounts[name])
        else:
            print("Account not found.")
    elif choice == "5":
        sender = input("Enter your name: ")
        receiver = input("Enter receiver name: ")
        if sender not in accounts:
            print("Sender account not found.")
        elif receiver not in accounts:
            print("Receiver account not found.")
        else:
            amount = float(input("Enter transfer amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            elif amount > accounts[sender]:
                print("Insufficient balance.")
            else:
                accounts[sender] -= amount
                accounts[receiver] += amount
                print("Money transferred successfully!")
    elif choice == "6":
        print("Thank you for using banking system!")
        break
    else:
        print("Invalid choice. Please try again.")
