import pandas as pd

# Reading nato file and converting it to DF
file = pd.read_csv('nato_phonetic_alphabet.csv')
nato_df = pd.DataFrame(file)

# Creating a dict of the nato alphabet from DF
nato_dict = {row['letter']: row['code'] for index, row in nato_df.iterrows()}

# Getting user input
word = input("Please enter a word to be converted: ")

# Main program
if word.isalpha:
    
    # Create resulting list of phonetics
    result = [nato_dict[letter] for letter in word.upper()]

    # Printing result
    print(f"Here's the phonetic list for that word: {result}")

# Handle other inputs
else:
    print("Please try again with a proper word.")





