#prevent user from creating an object of that class
#compels a user to override abstract method in child class
#abstract method: which has a declaration but doesn't have an implementation
#a class which contain 1 or more abstract method
#an abstract class is designed to be a blueprint for other classes. 

from abc import ABC, abstractmethod  # abstract base class

class Vehicle(ABC):  # parent class 

    @abstractmethod  # abstract method
    def go(self):  
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive a car")

    def stop(self):
        print("This car is stopped")    

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")    

# Remove the instantiation of Vehicle
# vehicle = Vehicle()  # This will raise an error

car = Car()
motorcycle = Motorcycle()

# Use the car and motorcycle objects
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()

