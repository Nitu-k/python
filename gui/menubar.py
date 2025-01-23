from tkinter import*

def openFile():
    print("File has been open")
def saveFile():
    print("File has been saved")
def cut():
    print("cut!") 
def copy():
    print("copy!")
def paste():
    print("paste!")          

window =Tk()

# openImage=PhotoImage(file="file.png")
# saveImage=PhotoImage(file="save.png")
# exitImage=PhotoImage(file="exit.png")

menubar=Menu(window)
window.config(menu=menubar)

fileMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)#dropdown affect
fileMenu.add_command(label="Open",command=openFile)#clickable option
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)#image=exitImage,compound=Left)

editMenu=Menu(menubar,tearoff=0,font=("MV Boil",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

window.mainloop()
