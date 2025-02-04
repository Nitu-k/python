from tkinter import*
from time import*

def update():
    time_string=strftime("%I:%M:%S %p")#convert tuple rep time to astring 
    time_label.config(text=time_string) #update label with new time

    day_string=strftime("%A")
    day_label.config(text=day_string)

    date_string=strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)

window=Tk()

time_label=Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_label.pack()
day_label=Label(window,font=("Ink Free",25))
day_label.pack()
date_label=Label(window,font=("Ink Free",30))
date_label.pack()

update()

window.mainloop()