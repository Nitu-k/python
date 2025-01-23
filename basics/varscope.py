#scope variable is available in region it is created in
#global and locally scoped version of var can be created 
name="nitu"#global
def display_name():
    name="kumari"# variable inside a function (local scope- availabe inside the function it's created in)
    print(name)

display_name()

#print(name)  can't be accesed outside the function 
print(name)#global name is available 

#egb -local enclosed global builtin






