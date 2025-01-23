#derived class inherit froma nother derived class
class Organism:#parent of parent of parent class 

    alive=True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog (Animal): #derived child class inherited from another child class
    def bark(self):
        print("This dog is barking")

dog=Dog()
print(dog.alive)
dog.eat()
dog.bark()
#child class inherit from another child class 
# child has parent and parent of that parent is grandparent (assume)        




