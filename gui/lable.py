from tkinter import*
#label= an area widget taht hold text/image

window=Tk()

photo =PhotoImage(file='gui\\nitu.png')
label=Label(window,
            text="Do check out the linkedin page",
            font=('Arial',20,'bold'),
            fg='#00FF00',
            bg='black',
            relief=RAISED,
            bd=10,
            padx=20,
            pady=20,
            image=photo,
            compound='bottom')
label.pack()
# label.place(x=0,y=0)
window.mainloop()