class Car: #class name start capital
      # for llarger program create a diff module
   

    def __init__(self,make,model,year,color):#constructor : creates obj for us
        #self refer to current obj
        self.make=make
        self.model=model
        self.year=year
        self.color=color

    def drive(self):#self is an argument, drive is method
        print("This "+self.model +"is driving")
    def stop(self):
        print("This "+self.model+" has stopped")

#__in__ : method , pass in arguments and assin arguments to each objects attributes
#and reuse as blue print to create more objects