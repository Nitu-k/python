#display star pattern
#* ** *** **** on different line
print("Enter value of n")
n=int(input())
for i in range(0,n): #bottomup star  (n,o,-1)
    for j in range(0,i+1):    #bottomup star (0,i-1)
        print('*',end="")
    print("")    