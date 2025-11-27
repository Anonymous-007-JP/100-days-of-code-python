# Asking user for input
import random

User_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor \n"))
# assign rock, scissor, paper as a graphic

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

all_scissor = [rock,paper,scissors]
while True:
  if User_input == 0:
      print(rock)
      break
  elif User_input ==1:
      print(paper)
      break
  elif User_input == 2:
      print(scissors)
      break
  else:
      print("Invalid input. Please Try again")
      User_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor \n"))

# Mistake it takes asics (drawing)  not input like 0 1 2  need to change this
# Computer_choice = random.choice(all_scissor)
Computer_choice = random.randint(0,2)
print(f"Computer Choose \n{all_scissor[Computer_choice]}")

if User_input == Computer_choice:
    print("Result tie")
elif (User_input == 0 and Computer_choice == 2) or (User_input == 1 and Computer_choice == 0) or (User_input == 2 and Computer_choice == 1):
    print("You win")
else:
    print("You lose")
