# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))
# operation = input("Choose + or -: ")

# if operation == "+":
#     answer = number1 + number2
#     print("The answer is", answer)
# elif operation == "-":
#     answer = number1 - number2
#     print("The answer is", answer)
# else:
#     print("Invalid choice.")

score = float(input("Enter a score from 0 to 100: "))

if score < 0:
    print("The score cannot be below 0.")
elif score > 100:
    print("The score cannot be above 100.")
elif score >= 70:
    print("You passed!")
else:
    print("You did not pass.")