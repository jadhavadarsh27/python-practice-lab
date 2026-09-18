class Animal:
    def sound(self):
        print("Makes sound")

class Dog(Animal):
    def sound(self):
        print("Barking")

class Cat(Animal):
    def sound(self):
        print("Meowing")

d = Dog()
c = Cat()

d.sound()
c.sound()
