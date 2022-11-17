from tkinter import *
from tkinter import ttk
import fitz
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageColor

class RenderLeaderBoard:
    def __init__(self , Matched , Mismatches , Statistics):

        self.Student_Data = { **Matched , **Mismatches }
        self.Stats = Statistics

        root = Tk()
        root.geometry('300x340')
        root.title("Megurine")

        self.terminal = Text( root , height=24 , width=39 )
        self.terminal.place( x=10 , y=10 )

        root.after( 500 , self.render )
        root.mainloop()


    def render(self):

        SD = self.getSortedLeaderBoard()

        self.terminal.insert( "end" , "\nStarted Rendering...\n\n----------\n\n" )

        DateFont = ImageFont.truetype("res/Fonts/calibri.ttf", 64)
        DateColor = (25, 25, 25)
        DatePosition = (1240, 420)

        StatsSize = 56
        StatsFont = ImageFont.truetype("res/Fonts/calibri.ttf", StatsSize)
        StatsColor = (150, 150, 150)

        TableFont = ImageFont.truetype("res/Fonts/calibri.ttf", 50)
        TableColor = (75, 75, 75)

        ClassFont = ImageFont.truetype("res/Fonts/calibrib.ttf", 60)
        ClassColor = (77, 119, 201)

        self.terminal.insert( "end" , "\nLoaded Fonts." )

        LeaderBoardBase = Image.open("res/LEADERBOARD.jpg")
        LeaderBoardEditor = ImageDraw.Draw(LeaderBoardBase)

        ClassWiseHeaderBase = Image.open("res/CLASSWISE_HEADER.jpg")
        ClassWiseHeaderEditor = ImageDraw.Draw(ClassWiseHeaderBase)

        ClassWiseBlankBase = Image.open("res/CLASSWISE_BLANK.jpg")
        ClassWiseBlankEditor = ImageDraw.Draw(ClassWiseBlankBase)

        ClassWiseTop = Image.open("res/CLASSWISE_TOP.jpg")
        ClassWiseDark = Image.open("res/CLASSWISE_DARK.jpg")
        ClassWiseLight = Image.open("res/CLASSWISE_LIGHT.jpg")
        ClassWiseBottom = Image.open("res/CLASSWISE_BOTTOM.jpg")

        self.terminal.insert( "end" , "\nLoaded Images." )


        #Generate LeaderBoard
        #-------------------------------------------------------------------------------------------------


        self.terminal.insert( "end" , "\n\n\nStarted LeaderBoard...")

        LeaderBoardEditor.multiline_text(DatePosition, self.Stats['date'] , DateColor, font=DateFont, align="center", anchor="ms")


        LeaderBoardEditor.multiline_text((876, 687), self.Stats['signup'], StatsColor, font=StatsFont, align="left", anchor="ls")
        LeaderBoardEditor.multiline_text((876 + 280, 687 + 110), self.Stats['tot_signup'], StatsColor, font=StatsFont,
                                         align="left",
                                         anchor="ls")
        LeaderBoardEditor.multiline_text((876 - 39, 687 + 220), self.Stats['login'], StatsColor, font=StatsFont, align="left",
                                         anchor="ls")
        LeaderBoardEditor.multiline_text((876 + 200, 687 + 330), self.Stats['login_conv'], StatsColor, font=StatsFont,
                                         align="left",
                                         anchor="ls")
        LeaderBoardEditor.multiline_text((876 + 600, 687 + 440), self.Stats['submitted'], StatsColor, font=StatsFont,
                                         align="left",
                                         anchor="ls")

        Index = 0
        XPosition = 1725
        RowHeight = 176
        YPositions = sorted( [560, 1825, 2190, 1055, 1430] )

        for Leader in SD[:10]:
            Row = [ Leader['name'] , str(Leader['score']) , self.HHMMSS( Leader['time_taken'] ) , Leader['branch'] , Leader['section'] ]
            X = XPosition + (RowHeight * Index)
            for Col in range(0, len(Row)):
                Y = YPositions[Col]
                LeaderBoardEditor.multiline_text((Y, X), Row[Col], TableColor, font=TableFont, align="center",
                                                 anchor="ms")
            Index += 1

        self.terminal.insert( "end" , "\nSaving LeaderBoard Image..." )
        LeaderBoardBase.save("Images/LEADERBOARD_OUTPUT.jpg")

        self.terminal.insert( "end" , "\nProcessing LeaderBoard PDF...")
        LeaderBoardPDF = fitz.open()
        LeaderBoardPDF.insertPage(0)
        PagePix = LeaderBoardPDF[0].get_pixmap()
        Rect = fitz.Rect(0, 0, PagePix.width, PagePix.height)
        Pix = fitz.Pixmap("Images/LEADERBOARD_OUTPUT.jpg")
        Page = LeaderBoardPDF[0]
        Page.insertImage(Rect, filename="Images/LEADERBOARD_OUTPUT.jpg", overlay=True, keep_proportion=False)
        LeaderBoardPDF.save("OUTPUT/WCC - LEADERBOARD - " + self.Stats['date'] + ".pdf")
        self.terminal.insert( "end" , "\nFinished LeaderBoard.\n\n")



        #Generate ClassWise
        #-------------------------------------------------------------------------------------------------

        self.terminal.insert( "end" , "\n\nStarted ClassWise...")

        ClassWiseHeaderEditor.multiline_text((DatePosition[0], DatePosition[1] + 39), self.Stats['date'], DateColor,
                                             font=DateFont,
                                             align="center", anchor="ms")

        ClassWiseLeaderList ={}

        for Student in SD:
            key = f'{Student["branch"]} {Student["section"]}'
            if key not in ClassWiseLeaderList.keys():
                ClassWiseLeaderList[key] = [Student]
            else:
                ClassWiseLeaderList[key].append( Student )

        ClassWisePage = 1
        ClassWisePosition = 850
        Dark = True
        RowHeight = 176
        YPositions = [235, 780, 1490, 2060]

        ClassWisePages = []


        self.terminal.insert( "end" , "\nGenerating ClassWise Images\nProgress :" )
        for Class in sorted( ClassWiseLeaderList.keys() ):
            LeadersInClass = ClassWiseLeaderList[Class]

            if ClassWisePosition >= 2500:
                ClassWiseHeaderBase.save("Images/CLASSWISE_OUTPUT_" + str(ClassWisePage) + ".jpg")
                ClassWisePages.append("Images/CLASSWISE_OUTPUT_" + str(ClassWisePage) + ".jpg")
                print("\t" + ClassWisePages[-1])
                ClassWisePage += 1
                ClassWiseHeaderBase.paste(ClassWiseBlankBase)
                ClassWisePosition = 150
            ClassWiseHeaderBase.paste(ClassWiseTop, box=(0, ClassWisePosition))
            ClassWiseHeaderEditor.multiline_text((1240, ClassWisePosition + 125), ' '.join(Class), ClassColor,
                                                 font=ClassFont,
                                                 align="center", anchor="ms")
            ClassWisePosition += 376
            Dark = True
            Index = 1
            for LeaderIndex in range(len(LeadersInClass)):
                if Dark:
                    ClassWiseHeaderBase.paste(ClassWiseDark, box=(0, ClassWisePosition))
                    ClassWisePosition += 177
                else:
                    ClassWiseHeaderBase.paste(ClassWiseLight, box=(0, ClassWisePosition))
                    ClassWisePosition += 177
                CurLeader = [str(Index)] + [ LeadersInClass[LeaderIndex]['name'] , str(LeadersInClass[LeaderIndex]['score']) , self.HHMMSS( LeadersInClass[LeaderIndex]['time_taken'] ) ]

                for Col in range(4):
                    Y = YPositions[Col]
                    ClassWiseHeaderEditor.multiline_text((Y, ClassWisePosition - int(RowHeight / 2)), CurLeader[Col],
                                                         TableColor, font=TableFont, align="center", anchor="mm")
                Index += 1
                Dark = not Dark
                if ClassWisePosition >= 3070 and LeaderIndex + 1 != len(LeadersInClass):
                    ClassWiseHeaderBase.paste(ClassWiseBottom, box=(0, ClassWisePosition))
                    ClassWiseHeaderBase.save("Images/CLASSWISE_OUTPUT_" + str(ClassWisePage) + ".jpg")
                    ClassWisePages.append("Images/CLASSWISE_OUTPUT_" + str(ClassWisePage) + ".jpg")
                    print("\t" + ClassWisePages[-1])
                    ClassWisePage += 1
                    ClassWiseHeaderBase.paste(ClassWiseBlankBase)
                    ClassWisePosition = 150
                    ClassWiseHeaderBase.paste(ClassWiseTop, box=(0, ClassWisePosition))
                    ClassWiseHeaderEditor.multiline_text((1240, ClassWisePosition + 125), ' '.join(Class), ClassColor,
                                                         font=ClassFont, align="center", anchor="ms")
                    ClassWisePosition += 376

            ClassWiseHeaderBase.paste(ClassWiseBottom, box=(0, ClassWisePosition))
            ClassWisePosition += 190
        if ClassWisePosition != 150:
            ClassWiseHeaderBase.save("Images/CLASSWISE_OUTPUT_" + str(ClassWisePage) + ".jpg")
            ClassWisePages.append("Images/CLASSWISE_OUTPUT_" + str(ClassWisePage) + ".jpg")
            print("\t" + ClassWisePages[-1])

        ClassWisePDF = fitz.open()
        ClassWisePageNumber = 0
        Progress = 0
        self.terminal.insert( "end" , "\nGenerating ClassWise Pages\nProgress :" )
        for ImageAddress in ClassWisePages:
            ClassWisePDF.insertPage(ClassWisePageNumber)
            PagePix = ClassWisePDF[0].get_pixmap()
            Rect = fitz.Rect(0, 0, PagePix.width, PagePix.height)
            Page = ClassWisePDF[ClassWisePageNumber]
            Page.insertImage(Rect, filename=ImageAddress, overlay=True, keep_proportion=False)
            ClassWisePageNumber += 1
            if ClassWisePageNumber // len(ClassWisePages) > Progress:
                Progress += 1
                self.terminal.insert("end" , ("|" * int(39 * ClassWisePageNumber // len(ClassWisePages))))
        self.terminal.insert( "end" , "\nGenerated ClassWise Images" )
        ClassWisePDF.save("OUTPUT/WCC - CLASSWISE - " + self.Stats['date'] + ".pdf")
        self.terminal.insert("end", "\nSaved ClassWise PDF")



        self.terminal.insert( "end" , "\n\n----------\n\nDone Rendering!" )


    def getSortedLeaderBoard(self):
        SortedLB = sorted( self.Student_Data.values() , key=lambda x : x['index'])
        print( "\n\n\nSorted Students : \n" )
        for Student in SortedLB:
            print(Student)
        return SortedLB

    def HHMMSS(self, TimeTaken):
        HH = int(TimeTaken//3600)
        TimeTaken %= 3600
        MM = int(TimeTaken//60)
        TimeTaken %= 60
        SS = int(TimeTaken)
        return f'{HH}:{MM}:{SS}'
