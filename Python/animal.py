from abc import ABC,abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Dog(Animal):
    def move(self):
        print("I can walk and run")
class Cat(Animal):
    def move(self):
        print("I can walk and run")
R = Human()
R.move()
D = Dog()
D.move()
C = Cat()
C.move()

