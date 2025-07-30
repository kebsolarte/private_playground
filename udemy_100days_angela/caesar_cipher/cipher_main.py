import string

alphabet = list(string.ascii_lowercase) + [' ']

def encrypt(text, shift):
    encrypted_letters = []
    
    for letter in text:
        index = alphabet.index(letter)
        shifted_index = index + shift #troubleshoot
        shifted_letter = alphabet[shifted_index]
        encrypted_letters.append(shifted_letter)

    encrypted_word = "".join(encrypted_letters)

    return encrypted_word


def decrypt(text, shift):
    decrypted_letters = []

    for letter in text:
        index = alphabet.index(letter)
        shifted_index = index - shift
        shifted_letter = alphabet[shifted_index]
        decrypted_letters.append(shifted_letter)

    decrypted_word = "".join(decrypted_letters)

    return decrypted_word

while True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        word = encrypt(text, shift)
    elif direction == 'decode':
        word = decrypt(text,shift)
    elif direction == 'quit':
        break

    print(f"The {direction}d word is {word}.")
