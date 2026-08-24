class Animal:
    def sound(self):
        print("Aniaml")

class Dog(Animal):
    def bark(self):
        print("bark")

d = Dog()
d.sound()
d.bark()
