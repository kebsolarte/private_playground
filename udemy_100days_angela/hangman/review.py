import random

word_list = ['shaz', 'chewy', 'kevs']

chosen_word = random.choice(word_list)

# for checking
print(chosen_word)

# init iterators and displays
display = ['_' for i in chosen_word]
word = "".join(display)
lives = 6
game_over = False

while not game_over:
    print(f"Word: {word}")

    # user input
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        print('Nice guess!')
        for i, letter in enumerate(chosen_word):
            if guess == letter:
                display[i] = letter
        word = "".join(display)
    else:
        print('Aww, bad guess.')
        lives -= 1
        print(lives)


    if word == chosen_word:
        print("You won")
        game_over = True
    else:
        if lives == 0:
            print("You lost")
            game_over = True
        else: continue

