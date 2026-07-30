num = int(input("Enter a number: "))

if num <= 1:
    print("Its not Prime")
    
else:
    
    for i in range(2, num):
        if num % i == 0:
            print("Its Not Prime")
            break
        
    else:
        print("Its prime")


          
