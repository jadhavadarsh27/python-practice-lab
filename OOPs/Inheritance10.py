class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("meowing")

d = Dog()
c = Cat()

d.bark()
d.sound()


c.meow()
c.sound()
