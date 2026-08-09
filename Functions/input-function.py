def student():
    Name = input("Enter a Name")
    Age = input("Enter a Age")
    return Name, Age
Name, Age = student()
print("Name is: ", Name)
print("Age is: ", Age)
