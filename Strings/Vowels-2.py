text = input("Enter a text: ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count = count + 1

print(f"number of vowels is {count}" )
