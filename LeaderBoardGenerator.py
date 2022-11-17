import cefpython3
import platform
import sys
import time
import json

LeaderBoardData = "-"

class Visitor(object):
    def SetBrowser(self , B):
        self.browser = B

    def Visit(self, value):
        global LeaderBoardData
        #print( "Called" )
        LeaderBoardData = value
        self.browser.CloseBrowser(False)

V = Visitor()

class LoadHandler(object):

    def OnLoadingStateChange(self, browser, is_loading, **_):
        if not is_loading:
            #print('ready')
            browser.GetMainFrame().GetText(V)

def BrowserCode( event_name ):
    sys.excepthook = cefpython3.cefpython.ExceptHook  # To shutdown all CEF processes on error
    cefpython3.cefpython.Initialize()
    B = cefpython3.cefpython.CreateBrowserSync(
        url= f"https://www.hackerrank.com/rest/contests/{event_name}/leaderboard?offset=0&limit=300",
        window_title="F")
    V.SetBrowser( B )
    B.SetClientHandler(LoadHandler())
    cefpython3.cefpython.MessageLoop()
    cefpython3.cefpython.Shutdown()

def LoadLeaderBoard( event_name ):
    try:
        print( event_name )
        event_name = event_name.replace(' - ', '-')
        event_name = event_name.replace(' ', '-')
        BrowserCode( event_name )
        LeaderBoardJsonObj = json.loads(LeaderBoardData)
        return LeaderBoardJsonObj['models']
    except Exception as e:
        print( e )
        return None

