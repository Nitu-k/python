#classes can inherit attributes and functions from another class
#they form parent -child relation or child will receive everything parent has
class Animal:
    alive=True

    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")
#change in parent class can be seen in child class

#rabbit child , animal parent
class Rabbit(Animal) :
    def run(self):
        print("THis rabbit is running")
class Fish(Animal) :
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal) :
    def fly(self):
        print("This hawk is flying")

#create onj
rabbit=Rabbit()
fish=Fish()
hawk=Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()
