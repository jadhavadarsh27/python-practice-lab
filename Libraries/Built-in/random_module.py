import random

print("Random Number: ", random.randint(1, 10))
#for random numbers

print("Random Float: ",random.random())
#for random float numbers

fruits = ["Apple", "Banana", "Chiku", "Grapes"]
print("Random fruits: ", random.choice(fruits))
#for random choice from list

random.shuffle(fruits)
print(fruits)
#for shuffle list
