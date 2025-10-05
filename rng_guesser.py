import random

diffa = input("Choose a difficulty, easy, medium or hard: ").lower()
while diffa not in ["easy", "medium", "hard"]:
    diffa = input("Choose a valid difficulty: ")
if (diffa == "easy"):
    diff = 5
elif (diffa == "medium"):
    diff = 25
elif (diffa == "hard"):
    diff = 50


n = random.randint(1, diff)
answer = 0
guess = 1
answer = int(input(f"Guess number between 1 and {diff}."))
while (n != answer):
    answer = int(input("Try again: "))
    guess += 1
    if (answer < n):
        print("The number is bigger than your answer.")
    elif (answer > n):
        print("The number is smaller than your answer.")

print(f"You got it in {guess} guesses.")

nig = 1

