class Animal:
    def sound(self):
        print("Animal Makes sound")

class Dog(Animal):
    def sound(self):
        print("Barking")

animal = Animal()
dog = Dog()

animal.sound()
dog.sound()
