print(" To-do list")
tasks = []
while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
            number = int(input("Enter task number to remove: "))
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task removed successfully!")
            else:
                print("Invalid task number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")