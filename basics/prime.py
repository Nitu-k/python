#check if a number is prime number

#user input
print("Enter a number: ")
num=int(input())

#prime no >1
if num>1:
    #check factors
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            break
        else:
            print(num,"is a prime number")

#if input is less than 1 or equal to 1 , it is not prime
else:
    print(num,"is not a prime number")
            