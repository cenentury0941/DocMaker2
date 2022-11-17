from tkinter import *
from tkinter import ttk
import fitz
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageColor
from SourceCodeGenerator import GenerateSourceCode


class RenderEditorial:
    def __init__(self , Questions, Date):

        self.Questions = Questions
        self.Date = Date

        root = Tk()
        root.geometry('300x340')
        root.title("Megurine")

        self.terminal = Text( root , height=24 , width=39 )
        self.terminal.place( x=10 , y=10 )

        root.after( 500 , self.render )
        root.mainloop()

    def render(self):
        self.terminal.insert( "end" , "\nStarted Rendering...\n\n----------\n\n" )

        DateFont = ImageFont.truetype("res/Fonts/calibri.ttf", 64)
        DateColor = (25, 25, 25)
        DatePosition = (1240, 420)

        StatsSize = 56
        StatsFont = ImageFont.truetype("res/Fonts/calibri.ttf", StatsSize)
        StatsColor = (150, 150, 150)

        TableFont = ImageFont.truetype("res/Fonts/calibri.ttf", 50)
        TableColor = (75, 75, 75)

        ProblemFont = ImageFont.truetype("res/Fonts/calibrib.ttf", 60)
        ProblemSize = 60
        ProblemColor = (68,114,196)

        TitleFont = ImageFont.truetype("res/Fonts/calibri.ttf", 120)
        TitleColor = (68,114,196)
        TitleSize = 120

        self.terminal.insert( "end" , "\nLoaded Fonts." )


        EditorialBase = Image.open("res/EDITORIAL_BLANK.jpg")
        EditorialEditor = ImageDraw.Draw(EditorialBase)

        EditorialBlank = Image.open("res/EDITORIAL_BLANK.jpg")
        EditorialHeader = Image.open("res/EDITORIAL_HEADER.jpg")

        EditorialTop = Image.open("res/EDITORIAL_BOX_TOP.jpg")
        EditorialBottom = Image.open("res/EDITORIAL_BOX_BOTTOM.jpg")

        self.terminal.insert( "end" , "\nLoaded Images." )

        EditorialPosition = 850
        EditorialCol = 250
        EditorialSize = 50
        EditorialPage = 0
        FontSize = 25

        EditorialBase.paste(EditorialHeader)
        EditorialEditor.multiline_text(DatePosition, self.Date , DateColor, font=DateFont, align="center", anchor="ms")
        EditorialBase.paste(EditorialTop, (0, EditorialPosition - 150))

        EditorialPages = []

        first_question = True


        self.terminal.insert( "end" , "\nProcessing Questions:" )

        for Question in sorted(self.Questions.keys()):
            self.terminal.insert("end", f"\n - {Question} : ")
            if EditorialPosition > 2500:
                EditorialBase.paste(EditorialBottom, (0, EditorialPosition))
                EditorialPosition = 150
                EditorialBase.save("Images/EDITORIAL_OUTPUT" + str(EditorialPage) + ".jpg")
                EditorialPages.append("Images/EDITORIAL_OUTPUT" + str(EditorialPage) + ".jpg")
                print('\t' + EditorialPages[-1])
                EditorialPage += 1
                EditorialBase.paste(EditorialTop, (0, EditorialPosition-150))
            elif not first_question:
                EditorialBase.paste(EditorialBottom, (0, EditorialPosition))
                EditorialPosition += 250
                EditorialBase.paste(EditorialTop, (0, EditorialPosition - 100))

            EditorialPosition += 15

            EditorialEditor.multiline_text( ( 1240 , EditorialPosition ) , Question , ProblemColor, font=ProblemFont, align="center",
                                           anchor="ms")
            EditorialPosition += ProblemSize + 32

            EditorialEditor.multiline_text((1240, EditorialPosition), self.Questions[Question]['Title'], TitleColor, font=TitleFont,
                                           align="center",
                                           anchor="ms")
            EditorialPosition += TitleSize + 50

            if EditorialPosition > 3300:
                EditorialBase.paste(EditorialBottom, (0, EditorialPosition))
                EditorialPosition = 150
                EditorialBase.save("Images/EDITORIAL_OUTPUT" + str(EditorialPage) + ".jpg")
                EditorialPages.append("Images/EDITORIAL_OUTPUT" + str(EditorialPage) + ".jpg")
                print('\t' + EditorialPages[-1])
                EditorialPage += 1
                EditorialBase.paste(EditorialTop)

            for line in self.Questions[Question]['Desc'].split('\n'):
                EditorialEditor.multiline_text((1240, EditorialPosition), line, StatsColor,
                                               font=StatsFont,
                                               align="center",
                                               anchor="ms")
                EditorialPosition += int(StatsSize * 1.1)

                if EditorialPosition > 3300:
                    EditorialBase.paste(EditorialBottom, (0, EditorialPosition))
                    EditorialPosition = 150
                    EditorialBase.save("Images/EDITORIAL_OUTPUT" + str(EditorialPage) + ".jpg")
                    EditorialPages.append("Images/EDITORIAL_OUTPUT" + str(EditorialPage) + ".jpg")
                    print('\t' + EditorialPages[-1])
                    EditorialPage += 1
                    EditorialBase.paste(EditorialTop)

            EditorialEditor.multiline_text((1240, EditorialPosition), f"Solution in {self.Questions[Question]['Lang']}", ProblemColor,
                                           font=ProblemFont,
                                           align="center",
                                           anchor="ms")
            EditorialPosition += ProblemSize + 150

            for line in self.Questions[Question]['Code'].split('\n'):
                line += ' '*( 39 - len(line) )
                padding = 0
                for i in range(len(line)):
                    if line[i] == ' ' or line[i] == '\t':
                        padding += 1
                    else:
                        break
                EditorialPosition = self.renderText( EditorialBase , line , ( int(padding*5) , EditorialPosition ) )

                if EditorialPosition > 3300:
                    EditorialBase.paste(EditorialBottom, (0, EditorialPosition))
                    EditorialPosition = 300
                    EditorialBase.save("Images/EDITORIAL_OUTPUT" + str(EditorialPage) + ".jpg")
                    EditorialPages.append("Images/EDITORIAL_OUTPUT" + str(EditorialPage) + ".jpg")
                    print('\t' + EditorialPages[-1])
                    EditorialPage += 1
                    EditorialBase.paste(EditorialTop)

            first_question = False

            self.terminal.insert("end", f"Done \n")

        EditorialBase.paste(EditorialBottom, (0, EditorialPosition))
        EditorialPosition = 150
        EditorialBase.save("Images/EDITORIAL_OUTPUT" + str(EditorialPage) + ".jpg")
        EditorialPages.append("Images/EDITORIAL_OUTPUT" + str(EditorialPage) + ".jpg")
        print('\t' + EditorialPages[-1])
        EditorialPage += 1
        EditorialBase.paste(EditorialTop)

        self.terminal.insert("end", f"\nProcessing PDF File : ")

        EditorialPDF = fitz.open()
        EditorialPageNumber = 0
        Progress = 0
        for ImageAddress in EditorialPages:
            EditorialPDF.insertPage(EditorialPageNumber)
            PagePix = EditorialPDF[0].get_pixmap()
            Rect = fitz.Rect(0, 0, PagePix.width, PagePix.height)
            Page = EditorialPDF[EditorialPageNumber]
            Page.insertImage(Rect, filename=ImageAddress, overlay=True, keep_proportion=False)
            EditorialPageNumber += 1
            if EditorialPageNumber // len(EditorialPages) > Progress:
                Progress += 1
                print(("|" * int(100 * EditorialPageNumber // len(EditorialPages))), end='')
        EditorialPDF.save("OUTPUT/WCC - EDITORIAL - " + self.Date + ".pdf")

        self.terminal.insert("end", f"Done \n")


        self.terminal.insert( "end" , "\n\n----------\n\nDone Rendering!" )


    def renderText(self , Page , Text , position):
        GenerateSourceCode( Text )
        Code = Image.open("res/Code.png")
        Page.paste( Code , ( 150+(position[0]) , (position[1]) - 150))
        return position[1] + Code.size[1]








