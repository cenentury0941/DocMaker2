from tkinter import *
from tkinter import ttk
import Constants
from rendereditorial import RenderEditorial

class EditorialGen():
    def __init__(self):
        root = Tk()
        root.geometry('1024x640')
        root.title("Hatsune")

        self.Data ={}
        self.Data['Problem 1'] = { "Title" : "" , "Lang" : "" , "Desc" : "" , "Code" : "" }
        self.Data['Problem 2'] = { "Title" : "" , "Lang" : "" , "Desc" : "" , "Code" : "" }
        self.Data['Problem 3'] = { "Title" : "" , "Lang" : "" , "Desc" : "" , "Code" : "" }

        self.currentproblem = 1

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, columnspan=6, rowspan=5 )

        background_label = Label(mainframe)
        background_image = PhotoImage(file="res/EditorialGen.png")
        background_label['image'] = background_image
        background_label.grid(column=0, row=0, sticky=(N, W, E, S) , columnspan=6, rowspan=5)

        self.q1_button = Button( mainframe , text="Problem 1" , height=3 , width=30 , command=self.problemChanged1 )
        self.q1_button.place( x=30 , y=320 )

        self.q2_button = Button(mainframe, text="Problem 2", height=3, width=30, command=self.problemChanged2 )
        self.q2_button.place( x=30 , y=395 )

        self.q3_button = Button(mainframe, text="Problem 3", height=3, width=30, command=self.problemChanged3 )
        self.q3_button.place( x=30 , y=470 )

        self.q1_button['background'] = "#BBBBBB"
        self.q2_button['background'] = "#FBFBFB"
        self.q3_button['background'] = "#FBFBFB"

        gen_button = Button(mainframe, text="Generate", height=2, width=20, command=self.generateEditorial)
        gen_button.place( x=860 , y=590 )

        name_label = Label( mainframe , text="Title :" , bg="#FBFBFB" )
        name_label.config(font=("Courier", 12))
        name_label.place( x=370 , y=15 )

        self.title = Entry( mainframe , width=39 )
        self.title.config( font=("Courier", 12) )
        self.title.place( x=470 , y=15 )

        lang_label = Label(mainframe, text="Lang :", bg="#FBFBFB")
        lang_label.config(font=("Courier", 12))
        lang_label.place(x=370, y=55)

        self.lang = Entry(mainframe, width=39)
        self.lang.config(font=("Courier", 12))
        self.lang.place(x=470, y=55)

        desc_label = Label(mainframe, text="Desc :", bg="#FBFBFB")
        desc_label.config(font=("Courier", 12))
        desc_label.place(x=370, y=95)

        self.desc = Text(mainframe, width=39, height=6)
        self.desc.config(font=("Courier", 12))
        self.desc.place(x=470, y=95)

        code_label = Label(mainframe, text="Code :", bg="#FBFBFB")
        code_label.config(font=("Courier", 12))
        code_label.place(x=370, y=220)

        self.code = Text(mainframe, width=39, height=18)
        self.code.config(font=("Courier", 12))
        self.code.place(x=470, y=220)

        code_label = Label(mainframe, text="Date : ", bg="#83a8b4", fg="#FFFFFF")
        code_label.config(font=("Courier", 18))
        code_label.place(x=25, y=595)

        self.date = Entry(mainframe, width=24)
        self.date.config(font=("Courier", 18))
        self.date.place( x=140 , y=595 )

        self.root = root
        root.mainloop()

    def problemChanged(self , problemnumber):
        print(problemnumber)
        currentproblem = "Problem " + str(self.currentproblem)
        self.Data[currentproblem]['Title'] = self.title.get()
        self.Data[currentproblem]['Lang'] = self.lang.get()
        self.Data[currentproblem]['Desc'] = self.desc.get("1.0","end")
        self.Data[currentproblem]['Code'] = self.code.get("1.0","end")
        self.currentproblem = problemnumber

        self.title.delete(0,"end")
        self.lang.delete(0, "end")
        self.desc.delete("1.0", "end")
        self.code.delete("1.0","end")


        currentproblem = "Problem " + str(self.currentproblem)
        self.title.insert( 0 , self.Data[currentproblem]['Title'] )
        self.lang.insert( 0 , self.Data[currentproblem]['Lang'] )
        self.desc.insert( "1.0" , self.Data[currentproblem]['Desc'] )
        self.code.insert( "1.0" , self.Data[currentproblem]['Code'] )

    def problemChanged1(self):
        self.q1_button['background'] = "#BBBBBB"
        self.q2_button['background'] = "#FBFBFB"
        self.q3_button['background'] = "#FBFBFB"
        self.problemChanged(1)

    def problemChanged2(self):
        self.q2_button['background'] = "#BBBBBB"
        self.q1_button['background'] = "#FBFBFB"
        self.q3_button['background'] = "#FBFBFB"
        self.problemChanged(2)

    def problemChanged3(self):
        self.q3_button['background'] = "#BBBBBB"
        self.q2_button['background'] = "#FBFBFB"
        self.q1_button['background'] = "#FBFBFB"
        self.problemChanged(3)

    def generateEditorial(self):
        currentproblem = "Problem " + str(self.currentproblem)
        self.Data[currentproblem]['Title'] = self.title.get()
        self.Data[currentproblem]['Lang'] = self.lang.get()
        self.Data[currentproblem]['Desc'] = self.desc.get("1.0", "end")
        self.Data[currentproblem]['Code'] = self.code.get("1.0", "end")
        RenderEditorial( self.Data, self.date.get() )

