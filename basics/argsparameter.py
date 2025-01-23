#args= pack all argument in a tuple
#useful for a function to acept varing amount of args
# def add(num1,num2):
def add(*args):# '* ' is teh parameter args is just  a name 
    sum=0
    args=list(args)
    args[0]=0
#    args[0]=0#tuple doesn't support argument assignment

    for i in args: #tuple iterating
        sum+=i
    return sum    

print(add(1,2,3,4,5,6))



