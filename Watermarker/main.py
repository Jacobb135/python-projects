import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


def choose_image():
    filename = askopenfilename()
    with Image.open(filename) as bg_img:
        if bg_img.width > int(1280):
            width = 1280
        if bg_img.height > int(1280):
            height = 1280
        bg_img.resize(height, width)

    background_img = ImageTk.PhotoImage(bg_img)
    background_label = tkinter.Label(image=background_img)
    background_label.image = background_img
    background_label.place(x=0, y=0)

gui = Tk(className="Watermarker")
gui.geometry("1280x1280")
main_label = Label(gui, text="Welcome to Watermarker", font=("Arial", 25), pady=5)
main_label.pack()
image_label = Label(gui, text="Please select an image", font=("Arial", 14))
image_label.place(x=47, y=80)
entry_button = Button(text="Select File", command=choose_image)
entry_button.place(x=49, y=110)
gui.mainloop()
