from tkinter import *

def submit():
    print("The temperature is: "+str(scale.get())+" degree C")

window=Tk()

hotImage=PhotoImage(file='gui\\hot.png')
hotLabel=Label(image=hotImage)
hotLabel = Label(image=hotImage, width=80, height=80)  # Adjust the width and height as needed
hotLabel.pack()


scale=Scale(
             window,
             from_=100,
             to=0,
             length=600,
             orient=VERTICAL,#orientation of scale
             font=('Consolas',20),
             tickinterval=10,#add numeric indicator
            #  showvalue=0#hide current value
            resolution=5,
            troughcolor='#69EAFF',
            fg='#FF1C00',
            bg='black'
)
scale.pack()

coldImage=PhotoImage(file='gui\\cold.png')
coldLabel=Label(image=coldImage)
coldLabel = Label(image=coldImage, width=80, height=80)  # Adjust the width and height as needed
coldLabel.pack()

button=Button(window,text='submit',command=submit)

window.mainloop()