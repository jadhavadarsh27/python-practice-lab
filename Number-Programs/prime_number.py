num = int(input("Enter a number: "))

if num <= 1:
    print("Not prime")

for i in range(2, num):
    if num % i == 0:
        print("Its not.")
        break
    else:
        print("Its prime")

    
