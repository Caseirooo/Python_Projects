import random


def deposit():
    while True:
        amount = input("How much do you want to deposit?\n$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                balance += amount
                with open("balance.txt", "w") as f:
                    f.write(str(balance))
                break
            else:
                print("Amount has to be greater than 0.")
        else:
            print("Amount has to be a number.")


with open("balance.txt", "r") as f:
    balance = int(f.read())
while True:
    choice = int(input(
        "\nWhat do you want to do?\n1. Deposit\n2. Check Balance\n3. GOLD GOLD GOLD\n4. Quit\n"))
    if choice == 1:
        deposit()
    elif choice == 2:
        print(balance)
    elif choice == 3:
        break
    elif choice == 4:
        break
