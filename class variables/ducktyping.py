class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("THis duck is talking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("this chicken is clucking")

class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")        

duck=Duck()
chicken=Chicken()
person=Person()

person.catch(chicken)



