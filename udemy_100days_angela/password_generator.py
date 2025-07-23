# Password Generator Project
import random

# Set lists of letters, numbers, and symbols
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Main program
print("Welcome to the PyPassword Generator!")

# Ask for user preferences
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Build password from lists
# Remember: most list methods only modify the lists and return None
# ^This creates a problem when assigning list methods to variables
password = list()

# Choose random letters
# Angela's solution:
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
for n in range(0, nr_letters):
    random_letter = random.randint(0, len(letters) - 1)
    password.append(letters[random_letter])

# Choose random symbols
for n in range(0, nr_symbols):
    random_symbol = random.randint(0, len(symbols) - 1)
    password.append(symbols[random_symbol])

# Choose random numbers
for n in range(0, nr_numbers):
    random_number = random.randint(0, len(numbers) - 1)
    password.append(numbers[random_number])

# Print an easy level password - order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Remember: join is a string method, the "" inits the variable
ez_password = "".join(password)
print(f"Your easy password is: {ez_password}")

# Print a hard level password - order is randomised
# Shuffle is a func in random module
random.shuffle(password)
hard_password = "".join(password)
print(f"Your hard password is: {hard_password}")
