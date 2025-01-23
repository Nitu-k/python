#function written in 1 line using lambda keyword
# accepts any no. of arguments , but only has one expression
#lambda parameter: expression

# def double(x):
#     return x*2
#print(double(5))
double=lambda x:x*2
multiply=lambda x,y,z:x*y
add=lambda x,y,z:x+y+z
full_name=lambda first_name, last_name: first_name+" "+last_name
age_check=lambda age:True if age>=18 else False
print(age_check(18))
print(full_name("Nitu","Kumari"))
print(multiply(5,6,7))





