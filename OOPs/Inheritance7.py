class Animal:
    def sound(self):
        print("Animal Makes sound")

class Dog(Animal):
    def bark(self):
        print("Barking...")

d = Dog()

d.sound()
d.bark()
