#copy file()- copy content of file
#copy() +permission mode +destionation can be a directory
#copy2() does everthing copy() does + copy metadata(file's creation and modification time)
import shutil
shutil.copyfile('I:\\python\\basicsanuj\\file\\text.txt','copy.txt')#source, destination


