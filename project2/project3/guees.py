number = 5

while True:
    guess = int(input("Guess a number from 1 to 7: "))

    if guess == number:
        print("You got it!")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")