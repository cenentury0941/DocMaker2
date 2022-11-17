from tkinter import *
from tkinter import ttk

class SplashScreen():
    def __init__(self , duration=2500):
        root = Tk()
        root.geometry('640x640')
        root.title("Hatsune")

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        background_label = Label(mainframe)
        background_image = PhotoImage(file="res/SplashScreen.png")
        background_label['image'] = background_image
        background_label.grid(column=0, row=0, sticky=(N, W, E, S))

        self.root = root
        root.after( duration , self.terminate )
        root.mainloop()

    def terminate(self):
        self.root.destroy()
