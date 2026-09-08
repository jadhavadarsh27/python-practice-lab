num = int(input("Enter a number"))

if num <= 1:
    print("Not Prime")
else:
    
    for i in range(2, num):
        if num % i == 0:
            print("not prime")
            break
    else:
        print("Its's prime")
