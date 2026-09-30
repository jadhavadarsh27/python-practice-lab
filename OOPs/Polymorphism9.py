class Animal:
    def sound(self):
        print("Makes sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()
