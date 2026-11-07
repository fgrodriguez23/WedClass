cart = ["apple", "milk", "bread", "apple"]
print(len(cart))
print(cart[0])
print(cart[2])
cart.append("eggs")
print(cart)
cart.insert(1, "banana")
print(cart)



print(cart.count("apple"))
cart.remove("bread")
print(cart)
cart.sort()
print(cart)
cart.reverse()
print(cart)


inventory={
    "apple": 10,
    "bananas": 15,
    "milk": 5,
    "bread": 8
}
print(inventory)
print(inventory["apple"])
inventory["eggs"] = 12
print(inventory)

print(inventory.keys())
print(inventory.values())

for item in inventory.keys():
    print(item)
for amount in inventory.keys():
    print(amount)
    for item, amount in inventory.items():
        print(item, amount)

customers = {
    "001": {
        "name": "John",
        "items": ["apple", "milk"],
        "total": 15
    },
    "002": {
        "name": "Mike",
        "items": ["bread", "eggs"],
        "total": 20
    }
}

print(customers["001"]["name"])
print(customers["001"]["items"])
print(customers["002"]["total"])

#i learned how to add, remove, and modify items  list, how to sort and reverse a list, how to count occurrences of an item 
#i dont know what is my final project yet but i will be thinking about idiads but i fell like i will end up using lists and dictionaries
