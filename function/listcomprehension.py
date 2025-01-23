#new list with less syntax is list comprehension
#list=[expression for item in iterable]
#list=[expression if/else for item in iterable]


# squares=[]           #create empty list
# for i in range(1,11): #create a for loop
#     squares.append(i*i) #define wt each loop iteration shoould do..
# print(squares)
# #or
# squares=[i*i for i in range(1,11)] #list compre....
# print(squares)
#or 
students=[100,90,80,70,60,50,40,30,0]
# passed_students=list(filter(lambda x:x>=60,students))
passed_students=[i if i>=60 else "FAILED" for i in students]
print(passed_students)

