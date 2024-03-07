# TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
#
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Names/invited_names.txt", "r") as f:
    name_list = f.readlines()

with open("./Input/Letters/starting_letter.txt") as f:
    letter_contents = f.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as f:
            f.write(new_letter)
