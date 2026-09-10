class Animal:
    def sound(self):
        print("Animal")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog")

d = Dog()
d.sound()
