from tkinter import *
from tkinter import ttk
from Error import ErrorMessage
import Constants
import LeaderBoardGenerator
from renderleaderboard import RenderLeaderBoard

class LeaderBoardGen():
    def __init__(self):
        self.LeaderBoard = {}
        self.FormData = {}
        self.Mismatches = { 'GoogleForm' : [] , 'LeaderBoard' : [] }
        self.MergedData = {}
        self.MismatchesMerged = {}
        self.Matched = []
        self.Matched_List_Selected = ""
        self.Statistics = {}

        root = Tk()
        root.geometry('1024x640')
        root.title("Hatsune")

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, columnspan=6, rowspan=5)

        background_label = Label(mainframe)
        background_image = PhotoImage(file="res/LeaderBoardGen.png")
        background_label['image'] = background_image
        background_label.grid(column=0, row=0, sticky=(N, W, E, S), columnspan=6, rowspan=5)

        self.currentstate = Constants.LEADERBOARD_URL_STATE

        self.Url_Frame = ttk.Frame( root , height=580 , width=745 )
        self.Url_Frame.place( x=278 , y=0 )

        title_img = PhotoImage( file="res/Title.png" )
        title_label = Label( self.Url_Frame , image=title_img , height=163 , width=745 )
        title_label.place( x=0 , y=150 )

        self.title = Entry( self.Url_Frame , width = 39 )
        self.title.config( font=("Courier" , 18) )
        self.title.place( x=100 , y=390 )

        title_label = Label( self.Url_Frame , text="Enter the name of the event (refer image)" )
        title_label.config( font=( "Courier" , 12 ) )
        title_label.place( x=150 , y=360 )

        self.Show_Frame = ttk.Frame(root, height=580, width=745)
        self.Show_Frame.place(x=278, y=0)

        show_label = Label(self.Show_Frame, text="If the leaderboard has been detected, click next.")
        show_label.config(font=("Courier", 12))
        show_label.place(x=135, y=50)

        self.LeaderBoard_Strings = StringVar(value=[])
        show_list = Listbox(self.Show_Frame, height=25, width=72, listvariable=self.LeaderBoard_Strings)
        show_list.place( x=160 , y=100 )

        self.Form_Frame = ttk.Frame(root, height=580, width=745)
        self.Form_Frame.place(x=278, y=0)

        form_label = Label(self.Form_Frame, text="Enter The Data From The Google Form Below")
        form_label.config(font=("Courier", 12))
        form_label.place(x=140, y=50)

        self.formdata_text = Text( self.Form_Frame , width=72, height=32 )
        self.formdata_text.place(x=110, y=100)

        self.Mis_Frame = ttk.Frame(root, height=580, width=745)
        self.Mis_Frame.place(x=278, y=0)

        mis_label = Label(self.Mis_Frame, text="Following Participants couldn't be matched with form data")
        mis_label.config(font=("Courier", 12))
        mis_label.place(x=80, y=50)

        self.GF_label = Label( self.Mis_Frame , text="None Selected" , width=72 )
        self.GF_label.place( x=25 , y=100 )

        self.LB_label = Label(self.Mis_Frame, text="None Selected", width=32)
        self.LB_label.place(x=500, y=100)

        self.MisGf_Strings = StringVar(value=[])
        self.mis_gf_list = Listbox(self.Mis_Frame, height=10, width=72, listvariable=self.MisGf_Strings , selectmode="extended")
        self.mis_gf_list.place(x=50, y=130)
        self.mis_gf_list.bind( "<<ListboxSelect>>" , self.update_gf_label )


        self.MisLb_Strings = StringVar(value=[])
        self.mis_lb_list = Listbox(self.Mis_Frame, height=10, width=32, listvariable=self.MisLb_Strings , selectmode="extended")
        self.mis_lb_list.place(x=500, y=130)
        self.mis_lb_list.bind( "<<ListboxSelect>>" , self.update_lb_label )

        self.Matched_Strings = StringVar(value=[])
        self.matched_list = Listbox(self.Mis_Frame, height=12, width=107, listvariable=self.Matched_Strings)
        self.matched_list.place(x=50, y=350)
        self.matched_list.bind( "<<ListboxSelect>>" , self.matchedSelected )

        link_button = Button( self.Mis_Frame , text="link \/" , width = 15 , command=self.link )
        link_button.place( x=200 , y=310 )

        unlink_button = Button(self.Mis_Frame, text="/\ un-link", width=15, command=self.unlink )
        unlink_button.place(x=400, y=310)

        self.Stats_Frame = ttk.Frame(root, height=580, width=745)
        self.Stats_Frame.place(x=278, y=0)

        stat_label = Label(self.Stats_Frame, text="Enter The Values Expected :")
        stat_label.config(font=("Courier", 18))
        stat_label.place(x=80, y=39)

        stat1_label = Label(self.Stats_Frame, text="Date : ")
        stat1_label.config(font=("Courier", 12))
        stat1_label.place(x=80, y=80)

        self.S1 = Entry(self.Stats_Frame, width=30)
        self.S1.config(font=("Courier", 12))
        self.S1.place(x=325, y=80)

        stat2_label = Label(self.Stats_Frame, text="Sign Up Count : ")
        stat2_label.config(font=("Courier", 12))
        stat2_label.place(x=80, y=110)

        self.S2 = Entry(self.Stats_Frame, width=30)
        self.S2.config(font=("Courier", 12))
        self.S2.place(x=325, y=110)

        stat3_label = Label(self.Stats_Frame, text="Total Sign Up Count : ")
        stat3_label.config(font=("Courier", 12))
        stat3_label.place(x=80, y=140)

        self.S3 = Entry(self.Stats_Frame, width=30)
        self.S3.config(font=("Courier", 12))
        self.S3.place(x=325, y=140)

        stat4_label = Label(self.Stats_Frame, text="Login Count : ")
        stat4_label.config(font=("Courier", 12))
        stat4_label.place(x=80, y=170)

        self.S4 = Entry(self.Stats_Frame, width=30)
        self.S4.config(font=("Courier", 12))
        self.S4.place(x=325, y=170)

        stat5_label = Label(self.Stats_Frame, text="Login Conversion Rate : ")
        stat5_label.config(font=("Courier", 12))
        stat5_label.place(x=80, y=200)

        self.S5 = Entry(self.Stats_Frame, width=30)
        self.S5.config(font=("Courier", 12))
        self.S5.place(x=325, y=200)

        stat6_label = Label(self.Stats_Frame, text="Submitted Code : ")
        stat6_label.config(font=("Courier", 12))
        stat6_label.place(x=80, y=230)

        self.S6 = Entry(self.Stats_Frame, width=30)
        self.S6.config(font=("Courier", 12))
        self.S6.place(x=325, y=230)

        next_button = Button(mainframe, text="Next", height=2, width=20, command=self.nextState)
        next_button.place(x=860, y=590)

        back_button = Button(mainframe, text="Back", height=2, width=20, command=self.prevState)
        back_button.place(x=15, y=590)

        self.s1_button = Button(mainframe, text="Enter Event Name", height=2, width=30)
        self.s1_button.place(x=30, y=300)

        self.s2_button = Button(mainframe, text="Verify Leaderboard", height=2, width=30)
        self.s2_button.place(x=30, y=350)

        self.s3_button = Button(mainframe, text="Enter Form Data", height=2, width=30)
        self.s3_button.place(x=30, y=400)

        self.s4_button = Button(mainframe, text="Correct Mismatches", height=2, width=30)
        self.s4_button.place(x=30, y=450)

        self.s5_button = Button(mainframe, text="Enter Statistics", height=2, width=30)
        self.s5_button.place(x=30, y=500)


        self.s1_button['background'] = "#BBFFBB"
        self.s2_button['background'] = "#FBFBFB"
        self.s3_button['background'] = "#FBFBFB"
        self.s4_button['background'] = "#FBFBFB"
        self.s5_button['background'] = "#FBFBFB"

        self.leaderboardloaded = False
        self.updateState()
        self.root = root
        root.mainloop()

    def nextState(self):
        if not self.stateTransition():
            return
        if self.currentstate == Constants.STATISTICS_STATE:
            print( 'Generating Document' )
        else:
            self.currentstate += 1
            self.updateState()

    def prevState(self):
        if self.currentstate != Constants.LEADERBOARD_URL_STATE:
            self.currentstate -= 1
            self.updateState()

    def updateState(self):
        self.Url_Frame.place_forget()
        self.Show_Frame.place_forget()
        self.Form_Frame.place_forget()
        self.Mis_Frame.place_forget()
        self.Stats_Frame.place_forget()

        if self.currentstate == Constants.LEADERBOARD_URL_STATE :
            self.Url_Frame.place( x=278 , y=0 )
            self.s1_button['background'] = "#BBFFBB"
            self.s2_button['background'] = "#FBFBFB"
            self.s3_button['background'] = "#FBFBFB"
            self.s4_button['background'] = "#FBFBFB"
            self.s5_button['background'] = "#FBFBFB"
        elif self.currentstate == Constants.SHOW_LEADERBOARD_STATE:
            self.Show_Frame.place( x=278 , y=0 )
            self.s1_button['background'] = "#69AA69"
            self.s2_button['background'] = "#BBFFBB"
            self.s3_button['background'] = "#FBFBFB"
            self.s4_button['background'] = "#FBFBFB"
            self.s5_button['background'] = "#FBFBFB"
        elif self.currentstate == Constants.FORM_DATA_STATE:
            self.Form_Frame.place( x=278 , y=0 )
            self.s1_button['background'] = "#69AA69"
            self.s2_button['background'] = "#69AA69"
            self.s3_button['background'] = "#BBFFBB"
            self.s4_button['background'] = "#FBFBFB"
            self.s5_button['background'] = "#FBFBFB"
        elif self.currentstate == Constants.MISMATCHES_STATE:
            self.Mis_Frame.place( x=278 , y=0 )
            self.s1_button['background'] = "#69AA69"
            self.s2_button['background'] = "#69AA69"
            self.s3_button['background'] = "#69AA69"
            self.s4_button['background'] = "#BBFFBB"
            self.s5_button['background'] = "#FBFBFB"
        elif self.currentstate == Constants.STATISTICS_STATE:
            self.Stats_Frame.place( x=278 , y=0 )
            self.s1_button['background'] = "#69AA69"
            self.s2_button['background'] = "#69AA69"
            self.s3_button['background'] = "#69AA69"
            self.s4_button['background'] = "#69AA69"
            self.s5_button['background'] = "#BBFFBB"

    def remapLeaderboard(self , LeaderBoard):
        Remapped = {}
        for leader in LeaderBoard:
            Remapped[ leader['hacker'] ] = leader
        print( 'remapped : ' , Remapped )
        return Remapped

    def cleanFormdata(self , FormData):
        cleanData = []
        for Line in FormData:
            if len(Line) < 6:
                continue
            if Line[-1][0] == '@':
                Line[-1] = Line[-1][1:]
            if '@' in Line[-1]:
                Line[-1] = Line[-1][:Line[-1].index('@')]
            cleanData.append(Line)
        return cleanData

    def stateTransition(self):
        if self.currentstate == Constants.LEADERBOARD_URL_STATE:
            if self.leaderboardloaded:
                ErrorMessage( "Already Loaded" )
                return True
            event_name = self.title.get().strip()
            LeaderBoard = LeaderBoardGenerator.LoadLeaderBoard( event_name )
            if LeaderBoard == None or len(LeaderBoard) == 0:
                ErrorMessage("Error Loading\nLeaderboard")
                self.root.destroy()
                return False
            else:
                self.leaderboardloaded = True
                self.LeaderBoard = self.remapLeaderboard( LeaderBoard )
                leaderboard_choice = sorted( [ hacker for hacker in LeaderBoard ] , key=lambda x:x['index'])
                self.LeaderBoard_Strings.set( [ f'{hacker["rank"]} : {hacker["hacker"]}' for hacker in leaderboard_choice ] )
        elif self.currentstate == Constants.FORM_DATA_STATE:
            Form_Data = self.formdata_text.get( "1.0" , "end" ).split('\n')
            for i in range(len(Form_Data)):
                Form_Data[i] = Form_Data[i].strip().split('\t')
            Form_Data = self.cleanFormdata( Form_Data )
            for line in Form_Data:
                self.FormData[line[-1]] = line
            self.mergeData( self.MergedData , self.LeaderBoard , self.FormData )
        elif self.currentstate == Constants.MISMATCHES_STATE:
            self.mergeMismatched()
        elif self.currentstate == Constants.STATISTICS_STATE:
            self.Statistics['date'] = self.S1.get().strip()
            self.Statistics['signup'] = self.S2.get().strip()
            self.Statistics['tot_signup'] = self.S3.get().strip()
            self.Statistics['login'] = self.S4.get().strip()
            self.Statistics['login_conv'] = self.S5.get().strip()
            self.Statistics['submitted'] = self.S6.get().strip()
            RenderLeaderBoard( self.MergedData , self.MismatchesMerged , self.Statistics  )
        return True

    def mergeData(self , dest , lb , gf ):
        self.Mismatches = { 'GoogleForm' : [] , 'LeaderBoard' : [] }

        for key in lb.keys():
            if key in gf.keys():
                leaderboard_data = { 'score' : lb[key]['score'] , 'rank' : lb[key]['rank'] , 'time_taken' : lb[key]['time_taken'] , 'index' : lb[key]['index'] }
                form_data = { 'name' : gf[key][-4] , 'branch' : gf[key][-3] , 'section' : gf[key][-2] , 'id' : gf[key][-1] }
                dest[key] = { **leaderboard_data , **form_data }
                print( dest[key] )
        for key in gf.keys():
            if key not in dest.keys():
                self.Mismatches['GoogleForm'].append( f'{key} | {gf[key][-4]} | {gf[key][-5]}' )
        print( self.Mismatches['GoogleForm'] )

        for key in lb.keys():
            if key not in dest.keys():
                self.Mismatches['LeaderBoard'].append( key )

        self.Mismatches['GoogleForm'] = sorted(self.Mismatches['GoogleForm'] , key = lambda x : x.lower())
        self.Mismatches['LeaderBoard'] = sorted(self.Mismatches['LeaderBoard'] , key = lambda x : x.lower())
        self.MisGf_Strings.set(self.Mismatches['GoogleForm'])
        self.MisLb_Strings.set(self.Mismatches['LeaderBoard'])
        self.Matched_Strings.set([])

        print( self.Mismatches['LeaderBoard'] )

    def update_gf_label(self , arg ):
        selected = self.mis_gf_list.curselection()
        if len(selected) == 0:
            pass
        else:
            self.GF_label['text'] = self.Mismatches['GoogleForm'][selected[0]]

    def update_lb_label(self, arg):
        selected = self.mis_lb_list.curselection()
        if len(selected) == 0:
            pass
        else:
            self.LB_label['text'] = self.Mismatches['LeaderBoard'][selected[0]]

    def link(self):
        try:
            GF = self.GF_label['text']
            LB = self.LB_label['text']
            self.Mismatches['GoogleForm'].remove( GF )
            self.Mismatches['LeaderBoard'].remove( LB )
            self.MisGf_Strings.set( self.Mismatches['GoogleForm'] )
            self.MisLb_Strings.set( self.Mismatches['LeaderBoard'] )
            self.Matched.append( f'{GF.split(" | ")[0]} | {LB}' )
            self.Matched_Strings.set( self.Matched )
        except:
            print( 'Unable to link' )


    def unlink(self):
        try:
            tounlink = self.Matched_List_Selected
            self.Matched.remove(tounlink)
            GF , LB = tounlink.split( ' | ' )
            GF = f'{GF} | {self.FormData[GF][-4]} | {self.FormData[GF][-5]}'
            self.Mismatches['GoogleForm'].append(GF)
            self.Mismatches['LeaderBoard'].append(LB)
            self.MisGf_Strings.set( self.Mismatches['GoogleForm'] )
            self.MisLb_Strings.set( self.Mismatches['LeaderBoard'] )
            self.Matched_Strings.set( self.Matched )
        except:
            print( 'Unable to unlink' )

    def matchedSelected(self , var):
        self.Matched_List_Selected = self.Matched[self.matched_list.curselection()[0]]
        print( self.Matched_List_Selected )

    def mergeMismatched(self):
        self.MismatchesMerged = {}
        for value in self.Matched:
            GF_Key , LB_Key = value.split(' | ')
            leaderboard_data = {'score': self.LeaderBoard[LB_Key]['score'], 'rank': self.LeaderBoard[LB_Key]['rank'], 'time_taken': self.LeaderBoard[LB_Key]['time_taken'],
                                'index': self.LeaderBoard[LB_Key]['index']}
            form_data = {'name': self.FormData[GF_Key][-4], 'branch': self.FormData[GF_Key][-3], 'section': self.FormData[GF_Key][-2], 'id': self.FormData[GF_Key][-1]}
            self.MismatchesMerged[ LB_Key ] = { **leaderboard_data , **form_data }
        for key in self.MismatchesMerged.keys():
            print( f'Matched : {self.MismatchesMerged[key]}' )

