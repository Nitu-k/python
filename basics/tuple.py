#immutable data type 
#+,_ index allowed , slicing allowed
#group related data 
#ordered
student=("nitu","neel","keerti")
print(student.count("nitu"))
print(student.index("neel"))

for x in student:
    print(x)

if "neel" in student:
    print("neel is here")    

    