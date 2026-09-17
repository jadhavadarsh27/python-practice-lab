class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meowing")

d = Dog()
c = Cat()

d.sound()
c.sound()

d.bark()
c.meow()
