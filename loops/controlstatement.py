#loop control statement: chnage loops execution from normal sequence : break , continue ,pass
#break:used to terminate loop entirely
#continue: skips to next iteration of loop
#pass= does nothiing acts as a placeholder

while True:
    name=input("Enter your name: ")
    if name !="":
        break 
phone_number="123-13456-346"
for i in phone_number:
    if i =="-":
        continue
    print(i,end="")   

for i in range(1,21):
    if i==13:
        pass
    else:
        print(i)     
