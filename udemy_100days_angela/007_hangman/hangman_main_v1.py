import random
import os
from hangman_words import word_list
from hangman_art import logo, stages

# Function for clearing screen for every iteration of the loop
def clear_screen():
    # 'cls' for Windows, 'clear' for Mac/Linux
    #  os.name returns 'nt' for Windows and 'posix' on Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
# print(chosen_word) # For testing only

# Initializing counters/lists
display = ["_"] * len(chosen_word)
word = "".join(display)
lives = 6
end_of_game = False

# Ask the user to guess a letter and assign their answer to a variable called guess. Check if guess is one of the letters in the chosen_word.
while not end_of_game:
    clear_screen()
    print(logo)
    print("Welcome to hangman! Guess the word and save hangman!\n")
    print(f"Word: {word}")
    print(stages[lives])
    guess = input("Guess a letter: ").lower()
    
    # Ensures user input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter from the alphabet.")
        continue
    
    # Check if input was already guessed previously
    if guess in display:
        print(f"You've already guessed {guess}!")
        continue
    
    # Check if guess is in the chosen word
    for n in range(len(chosen_word)):
        if chosen_word[n] == guess:
            display[n] = guess
            print(f"You chose {guess}. Correct! It's in the word!")
    
    # Updates word
    word = "".join(display)

    # Condition for wrong letters
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"Game over! The word is {chosen_word}. You lose!")
            break
        else:
            print(f"You chose {guess}. Sorry, try again!")
            continue
    
    # Condition for correct answer
    if "_" not in display:
        end_of_game = True
        print(f"The word is {chosen_word}! You won!")
        
    