#display the result such as disntinction , 1st class,2nd class, pass, fail on marks entered by user
print("Enter your marks")
m=int(input())
if m>=75:
    print("Grade: Distinction")
elif m>=60:
    print("Grade:First Class") 
elif m>=50:
    print("Grade : second class") 
elif m>=40:  
    print("Grade: Pass")
else:
    print("Grade: fail") 

               