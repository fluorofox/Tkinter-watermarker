import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile
import customtkinter
from PIL import ImageTk, Image, ImageFont, ImageDraw

# ---------------------------- GLOBAL CONSTANTS ------------------------------- #
MAX_SIZE = (800, 600)

# ---------------------------- UI SETUP ------------------------------- #

class UploadImageWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Watermarker")
        self.maxsize(1000,1000)
        self.columnconfigure(0, weight = 1, uniform="a")
        self.s = ttk.Style()
        self.mainframe = ttk.Frame(self, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=("nsew"))
        self.logo = tk.PhotoImage(file="ginger_fox.png")
        self.s.configure("logo.TLabel", font="TkHeadingFont", foreground="grey")
        self.logo_label = ttk.Label(self.mainframe, text="FLUOROFOX WATERMARKER", image=self.logo, compound="top", style="logo.TLabel")
        self.logo_label.grid(column=0, row=0, sticky=("we"))
        self.current_image  = ttk.Label(self.mainframe, image="")
        self.current_image.grid(column=0, row=1)
        self.add_image_button  = ttk.Button(self.mainframe, text="Upload Image", command= lambda:self.add_image())
        self.add_image_button.grid(column=0, row=2)
        self.edit_window = None
        
    def add_image(self):
        self.file_path  = askopenfile(mode ='r', filetypes =[('Image Files', '.jpeg .jpg .png')])
        self.img = Image.open(self.file_path.name)
        self.orig = self.img
        self.img.thumbnail(MAX_SIZE)
        self.thumb = ImageTk.PhotoImage(self.img)
        self.current_image.config(image = self.thumb)
        self.current_image.image=self.thumb
        self.add_image_button.config(text="Change Image")
        self.start_edit_button = ttk.Button(self.mainframe, text="Continue to Edit", command= lambda:self.continue_to_edit())
        self.start_edit_button.grid(column=2, row=2)
        self.logo_label.grid(column=1, row=0, sticky=("we"), columnspan=3)
        self.current_image.grid(column=0, row=1, columnspan=3)
        
    def continue_to_edit(self):
        h, w, x, y = self.winfo_height(), self.winfo_width(), self.winfo_x(), self.winfo_y()
        self.withdraw()
        self.edit_window = EditWindow(self, self.orig, self.thumb, h, w, x, y)
        
class EditWindow(tk.Toplevel):
    def __init__(self, master, orig, thumb, h, w, x, y):
        super().__init__(master)
        self.thumb = thumb
        self.orig = orig
        self.title("Image Watermarker")
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.maxsize(1000,1000)
        self.columnconfigure(0, weight = 1, uniform="a")
        self.s = ttk.Style()
        self.mainframe = ttk.Frame(self, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=("nsew"))
        self.logo = tk.PhotoImage(file="ginger_fox.png")
        self.s.configure("logo.TLabel", font="TkHeadingFont", foreground="grey")
        self.logo_label = ttk.Label(self.mainframe, text="FLUOROFOX WATERMARKER", image=self.logo, compound="top", style="logo.TLabel")
        self.logo_label.grid(column=1, row=0, sticky="we")
        self.current_image  = ttk.Label(self.mainframe, image=self.thumb)
        self.current_image.grid(column=0, row=1, columnspan=3)
        self.add_text_button = ttk.Button(self.mainframe, text="Add Text", command= lambda:self.input_text())
        self.add_text_button.grid(column=2, row=2)
        self.add_image_button = ttk.Button(self.mainframe, text="Add Image", command= "")
        self.add_image_button.grid(column=0, row=2)
        
    def input_text(self):
        self.input_box = customtkinter.CTkInputDialog(text="Enter Your Text Here", title = "Text Watermark")    
        self.input_text = self.input_box.get_input()
        self.title_font = ImageFont.truetype("arial.ttf", 46)
        self.edit_image = ImageDraw.Draw(self.orig)
        self.edit_image.text((10, 10), self.input_text, fill=(255, 255, 255, 128), font=self.title_font)
        self.orig.save("Images/edited_image.png", quality=95)
        self.current_image.after(2000, self.show_pic())
        
    def show_pic(self): 
        self.edited_image = Image.open("Images/edited_image.png")
        self.edited_image.thumbnail(MAX_SIZE)
        self.new_image = ImageTk.PhotoImage(self.edited_image)
        self.current_image.config(image=self.new_image)
        
        

if __name__ == "__main__":
    app = UploadImageWindow()
    app.mainloop()