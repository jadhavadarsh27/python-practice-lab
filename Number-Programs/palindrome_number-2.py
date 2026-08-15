num = input("Enter a number: ")

rev = str(int(num))[::-1]

if num == rev:
    print("Given number is palindrome.")
else:
    print("Not palindrome")
