#logical operator
temp=int(input("What is the temperature outside?: "))
if (temp>=0 and temp<=30): #both needs to be true
    print("the temp is good today")
    print("go outside")
elif temp<0 or temp>30: #3if 1 is true entire is true 
    print("the temp is bad today")
    print("stay inside")   





