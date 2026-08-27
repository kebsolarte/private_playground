import random
import os

# define functions
# choose a number from 1 to 100
def set_number():
    number = random.randint(1, 100)
    return number

# check if guess is right
def check_guess(guess, number):
    if number > guess:
        return "Too low."
    elif number < guess:
        return "Too high."
    elif number == guess:
        return "Correct!"
    
# set number of allowable attempts
def attempts(choice):
    if choice == 'easy':
        return 10
    elif choice == 'hard':
        return 5
    else:
        return "Invalid"
    

# main program
game_over = False

while not game_over:
    print("Welcome to the number guessing game!")
    # asks for the level of difficulty
    difficulty = input("Set the level of difficulty (Easy/Hard): ").lower()

    # initialize the attempts and number
    attempts_left = attempts(difficulty)
    number = set_number()

    # main loop for guessing the number
    while attempts_left > 0:
        guess = int(input("\nI'm thinking a number from 1 and 100. What do you think is that number?: "))

        result = check_guess(guess, number)

        if result == "Correct!":
            print("Nice! You guessed the number!\n")
            break
        else:
            attempts_left -= 1
            
            # checks for the remaining attempts to decide whether to exit the loop or not
            if attempts_left > 0:
                print(f"{result}. Guess again. {attempts_left} attempts remaining.\n")
                continue
            else:
                print("Aww. You ran out of guesses!\n")
                break

    # asks if the player still want to play another game 
    continue_game = input("\nWould you like to continue playing? (Y/N): ").lower()

    if continue_game == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        game_over = True

        







