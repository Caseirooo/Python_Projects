import random

with open("balance.txt", "r") as f:
    balance = int(f.read())
while True:
    choice = int(input("\nWhat do you want to do?\n1. Deposit\n2. Check Balance\n3. GOLD GOLD GOLD\n4. Quit\n"))
    if choice == 1:
        amount = int(input("How much do you want to deposit\n"))
        balance += amount
        with open("balance.txt", "w") as f:
            f.write(str(balance))
    elif choice == 2:
        print(balance)
    elif choice == 3:
    elif choice == 4:
        break