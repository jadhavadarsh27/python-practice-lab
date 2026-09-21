class Animal:
    def sound(self):
        print("Animal")

class Dog(Animal):
    def bark(self):
        print("Bark")

class Cat(Animal):
    def meow(self):
        print("Cat")


d = Dog()
c = Cat()

d.sound()
c.sound()
d.bark()
c.meow()
