#multithreading =flow f execution , liek a seperate order of instruction
#1 thread run at a time :gil(global interpreter lock)
#io bound : program waits for external event i.e user input etc

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You study")


x=threading.Thread(target=eat_breakfast,args=())    
x.start()

y=threading.Thread(target=drink_coffee,args=())    
y.start()

z=threading.Thread(target=study,args=())    
z.start()

x.join()
y.join()
z.join()

# eat_breakfast()
# drink_coffee()
# study()    

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())


