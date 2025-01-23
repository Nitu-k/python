#walrus operator :=
# assign value to variable as apart of larger expression
#assign expression aka walrus operator

# happy=True
# print(happy)
# print(happy := True) #walrus operato
#  print(happy=True)------gives error 


#without walrus operator
# foods=list()
# while True:
#     food=input("What food do you like? : ")
#     if food=="quit":
#         break
#     foods.append(food)

#using walrus operator  or assignment operator
foods=list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)




