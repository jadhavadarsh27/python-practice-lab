class Animal:
    def sound(self):
        print("All Animals makes sound.....")

class Dog(Animal):
    def bark(self):
        print("Barking....")

d = Dog()

d.sound()
d.bark()
