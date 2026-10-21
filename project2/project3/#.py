
total = 0

count = int(input("How many prices? "))

if count > 0:
    for i in range(count):
        price = float(input("Enter a price: "))
        total = total + price

    average = total / count
    print("Average is:", average)
else:
    print("Enter a number greater than 0.")