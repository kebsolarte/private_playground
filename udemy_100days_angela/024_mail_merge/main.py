# Relative paths
LETTER_TEMPLATE_PATH = "Input/Letters/starting_letter.txt"
GUEST_PATH = "Input/Names/invited_names.txt"
OUTPUT_PATH = "Output/ReadyToSend"

# Get list of guests
with open(GUEST_PATH, mode='r') as file:
    guest_list = [line.strip() for line in list(file.readlines())]

# Better/cleaner version of the line above since list() is redundant and .readlines() is not needed.
# .readlines() method is not memory efficient!
# with open(GUEST_PATH, mode="r") as file:
#     guest_list = [line.strip() for line in file]

# Open template
with open(LETTER_TEMPLATE_PATH, mode="r") as file:
    letter_template = file.read()

# Main write program
for guest in guest_list:

    # Fill in template with guest name
    filled_letter = letter_template.replace("[name]", guest)

    # Create output path for each letter
    output_file_path = f"{OUTPUT_PATH}/{guest}.txt"

    # Write letter to output path
    with open(output_file_path, mode='w') as file:
        file.write(filled_letter)



