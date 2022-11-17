from tkinter import *
from tkinter import ttk
import Constants

class WelcomeScreen():
    def __init__(self, UserInput):
        self.UserInput = UserInput
        root = Tk()
        root.geometry('1024x640')
        root.title("Hatsune")

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, columnspan=6, rowspan=8 )

        background_label = Label(mainframe)
        background_image = PhotoImage(file="res/WelcomeScreen.png")
        background_label['image'] = background_image
        background_label.grid(column=0, row=0, sticky=(N, W, E, S) , columnspan=6, rowspan=8)

        Leaderboard_button_icon = PhotoImage( file="res/LeaderBoardGen_Button.png" )
        leaderboard_button = Button( mainframe , command=self.leaderBoardSelected , padx=0 , pady=0 , bd=3 , width=342 , height=214, image=Leaderboard_button_icon, bg="#FBFBFB")
        leaderboard_button.grid( column = 1 , row = 6 , sticky=(E))

        Editorial_button_icon = PhotoImage( file="res/EditorialGen_Button.png" )
        editorial_button = Button(mainframe,  command=self.editorialSelected , padx=0 , pady=0 , bd=3 , width=342 , height=214, image=Editorial_button_icon, bg="#FBFBFB")
        editorial_button.grid(column=4, row=6 , sticky=(W))

        self.root = root
        root.mainloop()

    def leaderBoardSelected(self):
        self.UserInput['Welcome_Action'] = Constants.LEADERBOARD
        self.root.destroy()

    def editorialSelected(self):
        self.UserInput['Welcome_Action'] = Constants.EDITORIAL
        self.root.destroy()

