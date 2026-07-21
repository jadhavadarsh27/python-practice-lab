text = input("Enter a text: ")

text1 = str(text)[::-1]

if text == text1:
    print("Given string is palindrome.")

else:
    print("Given string is not palindrome.")
