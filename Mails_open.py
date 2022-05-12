# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as f:
    names = f.readlines()  # создаёт список

with open("./Input/Letters/starting_letter.txt") as t:
    t = t.read()
    for name in names:
        stripped_name = name.strip()  # убирает лишние пробелы
        new_letter = t.replace(PLACEHOLDER, stripped_name)  # заменяет константу на имя
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as comlited_letter:
            comlited_letter.write(new_letter)


