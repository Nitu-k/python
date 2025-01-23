#instance variable :declarede inside the constructor , each var having unique value
# class var declared inside class and outside cunstructor

#instance is defined inside constructor given unique value 
#class var : declared within class outside const. default value for all instance of class for all object ,
# which can be changed

class Car:
    wheels=4 #class variable

    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model#inst... var
        self.year=year
        self.color=color #instance variable


        