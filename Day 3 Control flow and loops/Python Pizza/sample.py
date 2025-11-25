print("Welcome to Python Pizza Deliveries!")
bill = 0

# keep asking until valid input
while True:
    size = input("What size pizza do you want? S, M or L:\n ").lower()
    if size == "s":
        bill = 15
        print(f"That will be ${bill}")
        break
    elif size == "m":
        bill = 20
        print(f"That will be ${bill}")
        break
    elif size == "l":
        bill = 25
        print(f"That will be ${bill}")
        break
    else:
        print("You typed the wrong inputs, please try again.")

# once we break out of the loop, the rest of the code runs
pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n ").lower()
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:  # Covers M and L
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N:\n ").lower()
if extra_cheese == "y":
    bill += 1

print(f"Your Final bill is ${bill}.")
