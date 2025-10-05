import random

player = {"hp": 100, "attack": 20, "heal": 5, "block": 10}
enemy = {"hp": random.randint(60, 80), "attack": 15, "block": 5}
turn = 1
while player["hp"] > 0 and enemy["hp"] > 0:
    print(f"\nTurn {turn}")
    print(f"Your HP: {player['hp']}, Enemy HP: {enemy['hp']}")
    action = input("Choose your action:\n1. Attack\n2. Heal\n3. Block\n")
    if action == "1":
        damage = player["attack"] - enemy["block"]
        enemy["hp"] -= damage
        print(f"You attacked the enemy for {damage} damage.")
    elif action == "2":
        player["hp"] += player["heal"]
        print(f"You healed yourself for {player['heal']} HP.")
    elif action == "3":
        player["block"] += 5
        print("You brace for the next attack, increasing your block.")
    else:
        print("Invalid action. You lose your turn.")

    if enemy["hp"] > 0:
        damage = enemy["attack"] - player["block"]
        player["hp"] -= damage
        print(f"The enemy attacked you for {damage} damage.")

    turn += 1
