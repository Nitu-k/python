name=input("what is your name?: ")# user input is string datatype
age=int(input("How old are you?: "))
height=input("How tall are you?: ")
age=age+1 #cause type error , concat workks for string only


print("Hello "+name)
#print("You are"+age+"years old") #int and string cant be concat
print("Your are "+str(age)+"years old")
print("You are "+str(height)+"cm tall")



