print("ATM simulation")
correct_pin = "1234"
balance = 100000
pin = input("Enter your pin: ")
if pin == correct_pin:
    print("Login successful!")
    while True:
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            print("Your balance:", balance)
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("Money deposited successfully!")
                print("Your balance:", balance)
            else:
                print("Amount must be greater than 0.")
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print("Money withdrawn successfully!")
                print("Your balance:", balance)
        elif choice == "4":
            print("Thank you for using ATM!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Incorrect pin!")
