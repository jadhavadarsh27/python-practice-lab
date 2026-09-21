class Animal:
    def sound(self):
        print("Animal")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()

d.sound()
