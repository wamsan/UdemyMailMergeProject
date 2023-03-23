#TODO: Create a letter using starting_letter.txt 


with open("Input/Names/invited_names.txt", "r") as line:
    names = line.readlines()
    for name in names:
        clean_name = name.strip()
        with open("Input/Letters/starting_letter.txt", "r") as letter:
            old_letter = letter.read()
            new_letter = old_letter.replace("[name]", clean_name)
            with open(f"Output/ReadyToSend/{clean_name}_invitation.txt", "x") as invitation:
                invitation.write(new_letter)


