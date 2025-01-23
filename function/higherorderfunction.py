#higer order function 
#accept function a s argument
#or returns a function
# In python obj are treated as function

def loud(text):# argument
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):#naming function func
    text=func("Hello")
    print(text)

hello(loud)#makes uppercase
hello(quiet)#makes lowercase

# example
#function return a function
def divisor(x):
    def dividend(y):
        return y/x 
    return dividend

divide=divisor(2)  #x=2 , we call divisor and return to function 
print(divide(10))


