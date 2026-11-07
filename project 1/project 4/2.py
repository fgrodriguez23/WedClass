def save_note(note, file_name):
    with open(file_name, "w") as file:
        file.write(note)
    return file_name


note = input("Type a short note: ")
file_name = save_note(note, "note.txt")
print("Your note was saved in", file_name)