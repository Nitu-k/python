#  **kwargs :puts argument in dictionary
# accept varing amount of keyword argument and pack them in dictionary
#args accept varing amount of positional argument and pack them in tuple

#def hello(first,last):
def hello(**kwargs):# ** matters not kwargs  that is just a name
#    print("Hello "+kwargs['first']+" "+kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():#print each word in different line
        print(value,end=" ")


hello(first="Nitu",middle="iqura",last="kumari")  #type error as middle element





