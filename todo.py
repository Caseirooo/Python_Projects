try:
    with open("tasks.txt", "r") as f:
        tasks = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    tasks = []

choice = 0
while True:
    choice = (input(
        "\nWhat do you want to do?\n1. Add a task\n2. View tasks\n3. Remove a task\n4. Quit\n"))
    if (choice == "1"):
        tasks.append(input("What's the new task?\n"))
    elif (choice == "2"):
        print("\n")
        for i in range(len(tasks)):
            print(f"{i+1}.{tasks[i]}")
        if not tasks:
            print("Your to-do list is empty.")
    elif (choice == "3"):
        if not tasks:
            print("Your to-do list is empty.")
        else:
            for i in range(len(tasks)):
                print(f"\n{i+1}.{tasks[i]}")
            try:
                remove_index = int(
                    input("\nWhich choice do you want to remove?\n")) - 1
                if 0 <= remove_index < len(tasks):
                    removed = tasks.pop(remove_index)
                    print(f"Removed: {removed}")
                else:
                    print("That number doesn't exist.")
            except ValueError:
                print("Please enter a valid number")
    elif (choice == "4"):
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")
        break
    else:
        input("Please insert a one of the following numbers:\n1. Add a task\n2. View tasks\n3. Remove a task\n4. Quit")
