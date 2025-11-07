import random
import os
from hangman_words import word_list
from hangman_art import logo, stages

# function for clearing screen for every loop iteration
#  cls for windows ui and clear for mac/linux
# os.name returns 'nt' for windows and 'posix' on linux/mac
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# randomly chooses a word from a word list
chosen_word = random.choice(word_list)

# initialize iterators and displays
display = ['_' for i in chosen_word]
word = "".join(display)
lives = 6
game_over = False
guesses = []

# main logic
while not game_over:
    # print game display
    clear_screen()
    print(logo)
    print("Welcome to hangman! Guess the word and save hangman!\n")
    print(f"Word: {word}")
    print(stages[lives])

    # ask for user input
    guess = input("Guess a letter: ").lower()

    # check if guess was already used
    if guess in set(guesses):
        print(f"You've already guessed the letter '{guess.upper()}'")
        continue

    # Ensures user input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter from the alphabet.")
        continue

    # add valid guess in guesses list
    guesses.append(guess)

    # check if the guess is in the chosen word
    # condition if it is right guess
    if guess in chosen_word:
        print(f"Nice guess! '{guess.upper()}' is in the word!")

        # update display
        for i, letter in enumerate(chosen_word):
            if guess == letter:
                display[i] = letter
        
        word = "".join(display)

        # check if all letters have been guessed
        if word == chosen_word:
            print(f"You've guessed the word '{chosen_word}'! You won!")
            game_over = True
        else: continue

    # condition if guess is wrong
    else:
        lives -= 1
        
        # check if all lives have been used
        if lives == 0:
            print(f"Game over! The word is '{word}'. You lost!")
            game_over = True
        else: 
            print("Aww, bad guess. Keep trying!")
            continue

