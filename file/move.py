#move
import os
source="I:\\python\\basicsanuj\\file\\test.txt "
destination="C:\\Users\\nitu\\Desktop"
try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(source,destination)
        print(source+"was moved")    
    
except FileNotFoundError:
    print(source+"was not found")



