#to comapre two number using nested condition
print("Enter value of a")
a=int(input())
print("Enter value of b")
b=int(input())
if a==b:
    print("Both the numbers are equal")
else:
    if a<b:
        print("a is less than b")
    else:
        if a>b:
            print("a is greater than b")        