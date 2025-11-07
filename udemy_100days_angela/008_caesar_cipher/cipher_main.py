import string

# construct a list of alphabet letters plus space character
alphabet = list(string.ascii_lowercase) + [' ']

# define the encrypt function
def encrypt(text, shift):
    encrypted_word= ""
    
    # checks the index of each letter and shifts the index using the specified shift
    # module expression makes sure that the program loops through alphabet when index is exceeded
    for letter in text:
        index = alphabet.index(letter)
        shifted_index = index + shift 
        shifted_index %= len(alphabet)
        shifted_letter = alphabet[shifted_index]
        encrypted_word += shifted_letter

    return encrypted_word


# define the decrypt function
def decrypt(text, shift):
    decrypted_word = ""

    # checks the index of each letter and shifts the index back
    for letter in text:
        index = alphabet.index(letter)
        shifted_index = index - shift
        shifted_letter = alphabet[shifted_index]
        decrypted_word = shifted_letter

    return decrypted_word


# main program
while True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    
    if direction == 'quit':
        break
    elif direction in ['encode', 'decode']:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if direction == 'encode':
            word = encrypt(text, shift)
        elif direction == 'decode':
            word = decrypt(text,shift)
    else:
        print("Wrong choice.")
        break

    print(f"The {direction}d word is {word}.")
