# def save_note(note, file_name):
#     with open(file_name, "w") as file:
#         file.write(note)
#     return file_name


# note = input("Type a short note: ")
# file_name = save_note(note, "note.txt")
# print("Your note was saved in", file_name)




def add_numbers(number1, number2):
    answer = number1 + number2
    return answer


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

answer = add_numbers(number1, number2)
print("The answer is:", answer)
