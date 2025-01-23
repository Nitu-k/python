#allow subclass(child class) to provide specific implekmentation which is already provided by parents class
class Animal:
    def eat(self):
        print("This animal is eating")#parent class 

class Rabbit(Animal):# use method comes from itslef rather than parents  class
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit=Rabbit()
rabbit.eat()
#obj uses a method that is most clossly assosiated iwth its child class than its parents class
#it relies on itself rather than parents class 
