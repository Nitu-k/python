a=input()
u=0
l=0
for i in a:
    if i!='' and i.isupper():#i not equal to space
        u+=1
    elif i!='' and i.islower():
        l+=1
print(a)
print('Upper case character: ' +str(u))
print('Lower case characters: ' +str(l))
