name =input("what is your name? ")
with open("names.txt", "w") as file:
    file.write(name)
print("name saved!")