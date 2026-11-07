with open("myfile.txt", "w") as file:
    file.write("Hello\n")
    file.write("My name is Francisco \n")
    file.write("I am learning Python\n")

with open("myfile.txt", "r") as file:
    print(file.read())

with open("myfile.txt", "a") as file:
    file.write("\n\n")

with open("myfile.txt", "r") as file:
    print(file.read())