import random
# Assume there is a Toss selection in Cricket
# User makes a call
user_input = input("Please select heads or tails for the toss:\n").lower().strip()

# Randomly flip the coin (0 = heads, 1 = tails)
coin_result = "heads" if random.randint(0, 1) == 0 else "tails"

print(f"\nThe coin landed on: {coin_result}")

# Decide winner
if user_input == coin_result:
    print("You won the toss!")

    # Keep asking until user enters a valid choice
    while True:
        decision = input("Would you like to bat or bowl first?\n").lower().strip()
        if decision == "bat":
            print("You chose to bat first 🏏")
            break
        elif decision == "bowl":
            print("You chose to bowl first 🎯")
            break
        else:
            print("Invalid choice. Please type 'bat' or 'bowl'.")
else:
    print("You lost the toss.")
    # Opponent makes a random choice without using a list
    opponent_decision = "bat" if random.randint(0, 1) == 0 else "bowl"
    print(f"Opponent chose to {opponent_decision} first.")
