#object ha sattributes and methods . 
#attributes: what an object is or has
#methods: what an object can do 
#object-
#class:functions as a blue print that tells attributes and functions an object can have
#class can be created in main module or dedicated solely for class

from car import Car 

car_1=Car("Chevy","Corvette",2025,"blue")
car_2=Car("Ford","Mustang",2026,"red")
# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)

car_1.drive()
car_2.stop()

