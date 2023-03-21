import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


def choose_image():
    filename = askopenfilename()
    bg_img = Image.open(filename)
    bg_img.thumbnail((1280, 1280))
    background_img = ImageTk.PhotoImage(bg_img)
    background_label = tkinter.Label(image=background_img)
    background_label.image = background_img
    background_label.place(x=160, y=150)


gui = Tk(className="Watermarker")
gui.geometry("1600x1600")
main_label = Label(gui, text="Welcome to Watermarker", font=("Arial", 25), pady=5)
main_label.pack()
image_label = Label(gui, text="Please select an image", font=("Arial", 14))
image_label.place(x=47, y=80)
entry_button = Button(text="Select File", command=choose_image)
entry_button.place(x=49, y=110)
logo_label = Label(gui, text="Enter the Watermark logo", font=("Arial", 14))
logo_label.place(x=400, y=80)
logo_button = Button(text="Create Image")
logo_button.place(x=400, y=110)
gui.mainloop()

https://www.geeksforgeeks.org/python-pillow-creating-a-watermark/
https://stackoverflow.com/questions/44887576/how-can-i-create-a-drag-and-drop-interfaceg