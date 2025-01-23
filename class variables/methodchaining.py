#method chaining calls multiple method sequentially 
# each call performs an action on same object and return self
class Car:
    def turn_on(self):
        print("you start the engine")
        return self # python return none so this is an imp attribute for chaining method
    def drive(self):
        print("You step on the car")
        return self
    def brake(self):
        print("You step on the brakes")
        return self
    def turn_off(self):
        print("You turn off the engine")
        return self


car=Car()

#method chaining
 #backslash is for redability and code contuniation , if teh chian is loner it can be broken \.
car.turn_on()\
.drive().brake().turn_off()


#normal method
# car.turn_on()
# car.drive()