#str.format() help in displaying o/p in string
animal="cow"
item="moon"
#print("The "+animal+" jumped over the "+item)
#print("The {} jumped over the {}".format(animal,item))
#print("The {0} jumped over the {1}".format(animal,item))#positional argument
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))#keyword argument
#print("The {1} jumped over the {1}".format(animal,item))#positional

#{} format fields work a s placeholders for item
# indexing does the same task

text="The {} jumped over the {}"
print(text.format(animal,item))

name="nitu"
print("helllo , my name is {}".format(name))
#adding padding
print("helllo , my name is {:10}.nice to meet you".format(name))
print("helllo , my name is {:<10}.nice to meet you".format(name))#left align
print("helllo , my name is {:>10}.nice to meet you".format(name))#left align
print("helllo , my name is {:^10}.nice to meet you".format(name))#center


number=3.14159
print("The number pi is {:.2f}".format(number))#floating point number , 2 digit after decimal
num=1000000
print("The number is {:,}".format(num))#commas
print("The number is {:b}".format(num))#binary
print("The number is {:0}".format(num))#octal
print("The number is {:x}".format(num))#hexasecimal
print("The number is {:E}".format(num))#scientific





