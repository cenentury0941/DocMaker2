import LeaderBoardGenerator as lbgen
import splashscreen as splash
import welcomescreen as welcome
import editorialgen as editgen
import leaderboardgen as leadgen
import Constants
import json
from tkinter import *
from tkinter import ttk

User_input = {}

# Show splash screen for 2500ms
splash.SplashScreen( 2500 )

# Show welcome screen
welcome.WelcomeScreen( User_input )

print( User_input['Welcome_Action'] )

if User_input['Welcome_Action'] == Constants.EDITORIAL:
    # User Selected Editorial
    editgen.EditorialGen()
else:
    # User Selected Leaderboard
    leadgen.LeaderBoardGen()

print( 'done' )




