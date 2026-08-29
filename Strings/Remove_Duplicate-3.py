t = input("Enter a text: ")

text = t.lower()

result = " "

for ch in text:
    if ch not in result:
        result = result + ch

print(result)
