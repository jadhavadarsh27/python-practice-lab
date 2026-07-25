text = input("Enter a text: ")

result = "  "

for ch in text:
    if ch not in result:
        result = result + ch

print("after removing duplicate: ", result)
