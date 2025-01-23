import os
import shutil
path="empty_folder"
try:
    #os.rmdir(path)
    shutil.rmtree(path)#delete folder
except FileNotFoundError:
    print("That file was not found") 
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cant delete that using that function ")    
else:
    print(path+ "was deleted")