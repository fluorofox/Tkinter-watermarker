from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image

# ---------------------------- GLOBAL CONSTANTS ------------------------------- #
MAX_SIZE = (800, 600)

# ---------------------------- FUNCTIONS ------------------------------- #

def add_image():
    file_path  = askopenfile(mode ='r', filetypes =[('Image Files', '.jpeg .jpg .png')])
    img = Image.open(file_path.name)
    orig = ImageTk.PhotoImage(img)
    img.thumbnail(MAX_SIZE)
    thumb = ImageTk.PhotoImage(img)
    currentimage.config(image = thumb)
    currentimage.image=thumb
    addimagebutton.config(text="Change Image")
    starteditbutton = ttk.Button(mainframe, text="Continue to Edit", command= lambda:set_ui_to_edit())
    starteditbutton.grid(column=2, row=2)
    logolabel.grid(column=1, row=0, sticky=(W, E), columnspan=3)
    currentimage.grid(column=0, row=1, columnspan=3)
    
def add_logo():
    pass

def set_ui_to_edit():
    pass
    
    


# ---------------------------- METHOD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Image Watermarker")
root.maxsize(1000,1000)
s = ttk.Style()
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))

logo = PhotoImage(file="ginger_fox.png")
s.configure("logo.TLabel", font="TkHeadingFont", foreground="grey")
logolabel = ttk.Label(mainframe, text="FLUOROFOX WATERMARKER", image=logo, compound="top", style="logo.TLabel")
logolabel.grid(column=0, row=0, sticky=(W, E))
currentimage = ttk.Label(mainframe, image="")
currentimage.grid(column=0, row=1)
addimagebutton = ttk.Button(mainframe, text="Upload Image", command= lambda:add_image())
addimagebutton.grid(column=0, row=2)

root.columnconfigure(0, weight = 1, uniform="a")
root.rowconfigure(0, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()