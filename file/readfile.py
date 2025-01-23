#read file
try:
    with open('I:\\python\\basicsanuj\\file\\text.txt') as file:
      print(file.read())
      print(file.closed)  

except FileNotFoundError:
   print("that file was not found: (")        