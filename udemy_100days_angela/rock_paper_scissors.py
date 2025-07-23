import random

# ASCII art for the game
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

# List of the choices
choices = [rock, paper, scissors]

# Asking user input
while True:
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
  try:
    print(f"You chose: {choices[user_choice]}")
    break
  except:
    print("Invalid input. Try again")
    continue

# Determining computer's choice
computer_choice = random.randint(0,2)

print(f"Computer chose: {choices[computer_choice]}")

# Determining the winner
if user_choice == computer_choice:
  print("It's a draw!")
elif user_choice < computer_choice:
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  else:
    print("You lose!")
elif user_choice > computer_choice:
  if user_choice == 2 and computer_choice == 0:
    print("You lose!")
  else:
    print("You win!")