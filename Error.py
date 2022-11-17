from tkinter import *
from tkinter import ttk
import Constants

class ErrorMessage():
    def __init__(self, Message):
        self.root = Tk()
        self.root.geometry('240x84')
        self.root.title("Error :(")

        error_label = Label( self.root , text=Message, width=24 )
        error_label.config( font=( "Courier" , 12 ) )
        error_label.grid( row=0 , column=0 , sticky=( N , E , W ) )

        error_button = Button( self.root , width=24 , text="Okay", command=self.buttonClicked)
        error_button.grid( row=2 , column=0 , sticky=(S) )

    def buttonClicked(self):
        self.root.destroy()