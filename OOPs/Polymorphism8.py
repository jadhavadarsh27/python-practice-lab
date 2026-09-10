class Animal:
    def sound(self):
        print("Animal")

class Dog(Animal):
    def sound(self):
        print("Dog")

class Cat(Animal):
    def sound(self):
        print("Cat")

d = Dog()
c = Cat()

d.sound()
c.sound()
