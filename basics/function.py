#function is a block of code executed when it is called
# #modules
# import math
# print(math.pi)


#*** a function in Python can have only 2 arguments (x,y)
def hello(first_name,last_name,age):#list parameter in function to call it
    print("hello "+first_name+" "+last_name)
    print("you are "+str(age)+"years old")
    print("have a nice day")
#my_name="nitu"    
hello("nitu","kumari",21)    #calling , defining f'n with paramater









from math import cos
print(cos(3.14))


#user defined function
def greet(name,dish='Pasta'):
    print('Good morning,',name)
    print('Please eat',dish)

#call function
greet('nitu','Samosa')#parameter

#return from function
def sum_of_list(a):
    print('Calculating...')
    return sum(a)

marks=[45,16,87,98,45]
sum_of_marks=sum_of_list(marks)
print('my sum of marks',sum_of_marks)

#example
def greetings(names):
    for name in names:
        print('Hello', name)

names=['Anuj','Shivam','raj']   
greetings(names)     



