
# ask for hours and pay per hour
hours = float(input("How many hours did you work? "))
hourly_pay = float(input("How much do you earn per hour? "))

# multiply to get the total pay
total_pay = hours * hourly_pay

# show pay before taxes
print(f"Your pay before taxes is ${total_pay:.2f}.")