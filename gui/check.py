from tkinter import*

def display():
    if(x.get()):
        print("You agree!")
    else:
        print("You don't agree :(")    


window =Tk()
x=BooleanVar()

panda_photo=PhotoImage(file='gui\\panda.png')

check_button=Checkbutton(window,
                         text="I agree to something",
                         variable=x,
                         onvalue=True,
                         offvalue=False,
                         command=display,
                         font=('Arial',20),
                         fg='#00FF00',
                         bg='black',
                         activeforeground='#00FF00',
                         activebackground='black',
                         padx=25,
                         pady=10,
                         image=panda_photo,
                         compound='left')
check_button.pack()

window.mainloop()