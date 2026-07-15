class Animal:
    def sound(self):
        print("Animal makes sound")
        
class Dog(Animal):
    def sound(self):
        print("Bark..")

class Cat(Animal):
    def sound(self):
        print("Meowing...")

d = Dog()
c = Cat()

d.sound()
c.sound()
    
