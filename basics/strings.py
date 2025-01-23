#sequence of character 
#string class brings function
#IMMUTABLE: cant be changed

name="Nitu"
print(len(name))
print(name.find("i"))
paragraph=''' This is a 
multiline
string 
paragraph .this is for testing
''' # we can use """ """ or ''' ''' for string
print(paragraph)

#indexing to access string 
fruit='Apple'
print(fruit[0])
print(fruit[-1])

#substring , range of character
#slicing
s="abcde"
print(s[1:4])
print(s[1:5])
print(s[3:])
print(s[:4])
print(s[0:5:2])# staring index: ending length(index): steps
print(s[1:3])
print(s[::-1])
print(s[-1:0:-1]) #edcb doesn't include a since its exclusive not inclusive

#slice by indexing and slice()
#[start:stop:step]
#index
name="Nitu Kumari"
#first_name= name[0::]
last_name=name[4:8]
print(last_name)
reversed_name=name[::-1]
print(reversed_name)

#slice
website1="http://google.com"
website2="http://wikipedia.com"
slice=slice(7,-4)
print(website1[slice])
print(website2[slice])






#for loops with string
#concatnation
a="abc"
b="def"
c=a+b
print(c)
#multiply
c=a*2
print(c)

for my_char in a:
    print(my_char*2)# o/p: aa bb cc

#python string methods
password="abcd" #gives true or false as output
print(password.isalpha())    
#print true or false
s="1234"
print(s.isdigit())
#lower
s="ABCDE"
print(s.lower())

#strip
x='       bcd      '
print(x.lstrip())



