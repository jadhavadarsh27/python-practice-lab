from abc import ABC, abstractmethod

@abstractmethod
class Animal(ABC):
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "bark"

d = Dog()

print(d.sound())

