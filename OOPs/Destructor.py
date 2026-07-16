class Student:
    def __init__(self):
        print("Object is created")

    def __del__(self):
        print("Object is destroyed")

s = Student()
del s
