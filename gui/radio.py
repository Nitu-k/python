from tkinter import *
from PIL import Image, ImageTk  # Import Pillow modules for image handling

# List of food items
food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered a hamburger!")
    elif(x.get()==1):
        print("You ordered a hotdog!")    
    else:
        print("Huh?")      

# Create the main window
window = Tk()

# Resize images using Pillow
def resize_image(path, size):
    img = Image.open(path)  # Open the image
    img = img.resize(size, Image.ANTIALIAS)  # Resize the image
    return ImageTk.PhotoImage(img)  # Convert to Tkinter-compatible image

# Paths to images and resizing
pizzaImage = resize_image('gui\\pizza.png', (100, 100))  # Resize to 100x100 pixels
hamburgerImage = resize_image('gui\\hamburger.png', (100, 100))
hotdogImage = resize_image('gui\\hot-dog.png', (100, 100))

# List of resized images
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

# Create a variable to track the selected radio button
x = IntVar()

# Create and pack the radio buttons
for index in range(len(food)):
    radiobutton = Radiobutton(
        window,
        text=food[index],  # Text for the radio button
        variable=x,  # Grouping: all radio buttons share the same variable
        value=index,  # Unique value for each button
        padx=25,  # Padding on x-axis
        pady=25,  # Padding on y-axis
        font=("Impact", 50),  # Font styling
        image=foodImages[index],  # Add the resized image
        compound='left',  # Position the image to the left of the text
        command=order#set command of radio to function
    )
    radiobutton.pack(anchor=W)  # Align to the west (left)

# Run the application
window.mainloop()
