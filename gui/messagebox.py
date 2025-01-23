from tkinter import*
from tkinter import messagebox

def click():
    # messagebox.showwarning(title='WARNING!',message='You have a VIRUS!!')
    # messagebox.showinfo(title='This is an info message box',message='You are a human')
    # messagebox.showerror(title='ERROR',message='something went wrong :(')
    #  if messagebox.askokcancel(title='ask ok cancel',message='Do you care?'):
    # if messagebox.askretrycancel(title='ask ok cancel',message='Do you care?'):
    #       print('You do care')
    # else:
    #       print("You don't care")    
    # if messagebox.askyesno(title='ask yes or no',message='Do you like cake ?'):
    #     print("I lie cake too")
    # else:
    #     print("why dont you ")   
    # answer=messagebox.askquestion(title='ask a question',message='Do you like pie') 
    # if(answer=='yes'):
    #     print('I like pie')
    # else:
    #     print('Why dont you')  
    answer=messagebox.askyesnocancel(title='yesnocancel',message='Do you like coding')
    if(answer==True):
        print("You like to code")
    elif(answer==False):
        print("why ?")
    else:
        print("dodged..")        


     

window=Tk()

button=Button(window,command=click,text='click me')
button.pack()

window.mainloop()