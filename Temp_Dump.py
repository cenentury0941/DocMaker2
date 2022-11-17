
#choices = ["apple", "orange", "banana"]
#choicesvar = StringVar(value=choices)
#l = Listbox( mainframe , listvariable=choicesvar , height = 10)
#l.grid(column=2, row=1, sticky=(W, E))

def getLeaderBoard():
    eventname = "Weekly Code Challenge 03 - 06 Sept 2021 Third Year"
    eventname = eventname.replace( ' - ' , '-' )
    eventname = eventname.replace( ' ' , '-' )
    print( eventname )
    LeaderBoardJsonText = lbgen.LoadLeaderBoard( eventname )
    LeaderBoardJsonObj = json.loads( LeaderBoardJsonText )

    choices = []
    for hacker in LeaderBoardJsonObj['models']:
        print( hacker['hacker'] )
        choices.append( hacker['hacker'] )
    #choicesvar.set(choices)

#b = Button( mainframe , command = getLeaderBoard , text="Get LeaderBoard" )
#b.grid(column=3, row=2, sticky=(W, E))
