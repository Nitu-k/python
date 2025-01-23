# a=int(input())
# b=int(input())
# t=len(str(b))
# if (a%(int(pow(10,t)))==b):
#     print('yes')
# else:
#     print('no')   
 
#OR

def check_substring(a, b):
    # Convert both integers to strings
    str_a = str(a)
    str_b = str(b)
    
    # Check if str_b is a substring of str_a
    if str_b in str_a:
        return True
    else:
        return False

# Input integers
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))

# Output the result
result = check_substring(a, b)
print("Result:", result)
