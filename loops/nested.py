#nested : 1 loop inside another
#inner loop finishes all opearation before going to outer loop
rows=int(input("How many rows?: "))
columns=int(input("How many columns:? "))
symbol=input("Enter a symbol to use: ")

for i in range (rows):
    for j in range(columns):
        print(symbol,end="")# end stops code from going to next line
    print()    


