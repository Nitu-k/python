#break :to break out of loop
#continue keywprd : to skip current iteration in a loop , goes to next iteration
for i in range(10):
    if i>6:
        break
    print(i)

for i in range(10):
    if i ==8:
        continue # using this we skip 8
    print(i)