try:
    numerator=int(input("Enter a number to divide: "))
    denominator=int(input("Enter a number to divide by: "))
    result=numerator/denominator
    print(result)

except ZeroDivisionError as e:
    print(e)
    print("You cant divide by zero idiot!")

except ValueError as e:
    print(e)
    print("Enter only number please")   

except Exception as e:#not a good practice , handle specific error individually
    print(e)#shows exception as well , optional
    print("something went wrong")

else:
    print(result)

finally: #end clause  , always execute a block of code to close a file
    print("This wil always execute")







