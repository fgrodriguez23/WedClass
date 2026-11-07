# Intro to Programming
# Debug Exercise 3
#
# There are two problems here. One is quite obvious;
# the other is less so. If you need a hint
# send me a message on Canvas or email me ~Tom
#while True:
# This loop should output numbers from 1 through 10.
while True:
    print("Counting up: ", end=" ")

    for count in range(1, 11):
        print(count, end=" ")

    print("")

    choice = input("Should I print them again? (y/n) ")

    if choice.lower() == 'n':
        break
