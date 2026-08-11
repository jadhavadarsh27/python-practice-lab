import random

print("Random number: ", random.randint(1, 10))
print("Float number: ", random.random())

fruits = ["Apple", "Banana", "Chikuu", "Dragon"]
print("Random fruit: ", random.choice(fruits))

random.shuffle(fruits)
print(fruits)
