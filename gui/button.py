from tkinter import*

count=0

def click(): #define the function click ooutside window
    # print("You clicked the button!")
    global count
    count+=1
    print(count)

window=Tk()
photo=PhotoImage(file='gui\\great.png')

button=Button(window,
              text="click me!",
              command=click,
              font=("Comic Sans",30),
              fg="#00FF00",
              bg="black",
              activeforeground="#00FF00",#on clicking teh color remain same
              activebackground="black",
              image=photo,
              compound='bottom'
            #   state=DISABLED)#DONT LET ANYONE USE BUTTON
              
)

button.pack()

window.mainloop()