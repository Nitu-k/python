#file detection
import os
path="C:\\Users\\nitu\\Desktop\\text.txt"# backslash within a string needs double backslash not \ bt\\

if os.path.exists(path):
    print("that locationn exist")
    if os.path.isfile(path):
        print("that is a file")
else:
    print("Location doesnt exist")


