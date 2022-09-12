from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account #this is for the scopes/sheet access

import funcs
import random

playerslist = []

players = 0

def playercount():
    global players
    players = players + 1

class Player:
    def __init__(self, playername, Soloqueue, Flexqueue, Primary, Secondary, Duo):
        self.Name = playername
        self.Soloqueue = Soloqueue
        self.Flexqueue = Flexqueue
        self.Primary = Primary
        self.Secondary = Secondary
        self.Duo = Duo
        self.Elo = funcs.player_ELO(self)


class Team:
    def __init__(self, top, jg, mid, adc, supp):
        self.Top = top
        self.Jg = jg
        self.Mid = mid
        self.Adc = adc
        self.Supp = supp
        self.TeamElo = funcs.team_ELO(top, jg, mid, adc, supp)

def removal(obj, list):
    if(obj in list):
        list.remove(obj)

def userdata():
    return

#this function is 
def pulldata(sheetid, datarange):
    # sheets access through service account
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SERVICE_ACCOUNT_FILE = 'key.json'
    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID of a sample spreadsheet. 
    #spread sheet id is the the letters in the url between d/ and /edit
    SAMPLE_SPREADSHEET_ID = sheetid #to get this we will have to have some sorta of menu interface.

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        SAMPLE_RANGE_NAME = datarange #we will need to have user input for this
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        for row in values[1:]:
            playerslist.append(Player(row[0], row[1], row[2], row[3], row[4], row[5]))
            playercount()
    except HttpError as err:
        print(err)


def hi_low():
    playerslist.sort(key=lambda o: o.Elo)

    #for testing purposes just prints out object elo and name
    # for i in playerslist:
	#     print(i.Elo, i.Name)

    team = []
    high = False
    while(len(playerslist) != 0):
        team = []
        for i in range(players/5): # this needs to be changed when the number becomes off this is just here for filler
            if(high == False and len(playerslist) > 0):
                team.append(playerslist[0]) 
                high = True
                playerslist.pop(0)
            elif(high == True and len(playerslist) > 0):
                team.append(playerslist[-1])
                playerslist.pop()
                high = False
            else:
                return
        #print(len(playerslist))
        print("[",  end = "")
        for i in team:
	        print(i.Name, end = ", ")
        print("]")

def tourneymaker():
    top = []
    jg = []
    mid = []
    adc = []
    supp = []
    fill = []

    top2 = []
    jg2 = []
    mid2 = []
    adc2 = []
    supp2 = []

    fill2 = []
    TeamList = []

#this fills the lists above
    for i in playerslist:
        if i.Primary == "Top":
            top.append(i)
        elif i.Primary == "Jungle":
            jg.append(i)
        elif i.Primary == "Mid":
            mid.append(i)
        elif i.Primary == "ADC":
            adc.append(i)
        elif i.Primary == "Support":
            supp.append(i)
        else:
            fill.append(i)
    
    for i in playerslist:
        if i.Secondary == "Top":
            top2.append(i)
        elif i.Secondary == "Jungle":
            jg2.append(i)
        elif i.Secondary == "Mid":
            mid2.append(i)
        elif i.Secondary == "ADC":
            adc2.append(i)
        elif i.Secondary == "Support":
            supp2.append(i)
        else:
            fill2.append(i)
    
    
#prints list of primary roles for each role
    # print("[",  end = "")
    # for i in top:
    #     print(i.Primary, end = ", ")
    # print("]")

    # print("[",  end = "")
    # for i in jg:
    #     print(i.Primary, end = ", ")
    # print("]")

    # print("[",  end = "")
    # for i in mid:
    #     print(i.Primary, end = ", ")
    # print("]")

    # print("[",  end = "")
    # for i in adc:
    #     print(i.Primary, end = ", ")
    # print("]")

    # print("[",  end = "")
    # for i in supp:
    #     print(i.Primary, end = ", ")
    # print("]")

#this is what makes the teams, it picks randomly from all lists with priority order primary, secondary, primary fill, secondary fill
#they only move to the next if the current on is empty
    count =  players // 5 #this needs to be changed when the number becomes off this is just here for filler
    for i in range(count): 
        if(len(top) > 0):
            ctop = top[random.randrange(0, len(top))]
        elif(len(top2) > 0):
            ctop = top2[random.randrange(0, len(top2))]
        elif(len(fill) > 0):
            ctop = fill[random.randrange(0, len(fill))]
        else:
            ctop = fill2[random.randrange(0, len(fill2))]

#this runs a basic remove functions defeined above. could be changed to save space
        removal(ctop, top)
        removal(ctop, top2)
        removal(ctop, fill)
        removal(ctop, fill2)

        if(len(jg) > 0 ):
            cjg = jg[random.randrange(0, len(jg))]
        elif(len(jg2) > 0):
            cjg = jg2[random.randrange(0, len(jg2))]
        elif(len(fill) > 0):
            cjg = fill[random.randrange(0, len(fill))]
        else:
            cjg = fill2[random.randrange(0, len(fill2))]
        
        removal(cjg, top)
        removal(cjg, top2)
        removal(cjg, fill)
        removal(cjg, fill2)

        if(len(mid) > 0 ):
            cmid = mid[random.randrange(0, len(mid))]
        elif(len(mid2) > 0):
            cmid = mid2[random.randrange(0, len(mid2))]
        elif(len(fill) > 0):
            cmid = fill[random.randrange(0, len(fill))]
        else:
            cmid = fill2[random.randrange(0, len(fill2))]
        
        removal(cmid, top)
        removal(cmid, top2)
        removal(cmid, fill)
        removal(cmid, fill2)

        if(len(adc) > 0 ):
            cadc = adc[random.randrange(0, len(adc))]
        elif(len(adc2) > 0):
            cadc = adc2[random.randrange(0, len(adc2))]
        elif(len(fill) > 0):
            cadc = fill[random.randrange(0, len(fill))]
        else:
            cadc = fill2[random.randrange(0, len(fill2))]
        
        removal(cadc, top)
        removal(cadc, top2)
        removal(cadc, fill)
        removal(cadc, fill2)

        if(len(supp) > 0 ):
            csupp = supp[random.randrange(0, len(supp))]
        elif(len(supp2) > 0):
            csupp = supp2[random.randrange(0, len(supp2))]
        elif(len(fill) > 0):
            csupp = fill[random.randrange(0, len(fill))]
        else:
            csupp = fill2[random.randrange(0, len(fill2))]
        
        removal(csupp, top)
        removal(csupp, top2)
        removal(csupp, fill)
        removal(csupp, fill2)

#appends a team object in to a teamlist
        TeamList.append(Team(ctop, cjg, cmid, cadc, csupp))


#prints team comp by acessing a n object in the list of team objects
    for i in range(count):
        print(TeamList[i].Top.Name, TeamList[i].Top.Soloqueue)
        print(TeamList[i].Jg.Name, TeamList[i].Jg.Soloqueue)
        print(TeamList[i].Mid.Name, TeamList[i].Mid.Soloqueue)
        print(TeamList[i].Adc.Name, TeamList[i].Adc.Soloqueue)
        print(TeamList[i].Supp.Name, TeamList[i].Supp.Soloqueue)
        print(TeamList[i].TeamElo)
        print()


#prints list of primary roles for each role
    # print("[",  end = "")
    # for i in top:
    #     print(i.Primary, end = ", ")
    # print("]")

    # print("[",  end = "")
    # for i in jg:
    #     print(i.Primary, end = ", ")
    # print("]")

    # print("[",  end = "")
    # for i in mid:
    #     print(i.Primary, end = ", ")
    # print("]")

    # print("[",  end = "")
    # for i in adc:
    #     print(i.Primary, end = ", ")
    # print("]")

    # print("[",  end = "")
    # for i in supp:
    #     print(i.Primary, end = ", ")
    # print("]")
    


                
    
            


    
        
def main():
#main intake of data

    # rawstr = input("Copy and paste your Sheets link: ")
    
    # counter = 0
    # sheet_id = ""
    # for i in rawstr:
    #     if(counter == 5):
    #         sheet_id = sheet_id + i    
    #     if(i == '/' ):
    #         counter = counter + 1
    
    # sheet_id = sheet_id[:-1]

    # worksheet_name = input("Type in the Name of the Worksheet the data is on: ")
    # datarange = input("Number of players: ")

    # rangename = worksheet_name + '!' + "A1" + ":" + 'F' + datarange

    #pulldata(sheet_id, rangename)

#for quicker testing process
    
    pulldata("1p0fj3QFIBhk54o1GDFRe4sfroJJ3BQJX3Wgmrky7SUg", "Sheet1!A1:F26")

    print("players list")
    print("Avg Elo of All Players", + funcs.total_average_elo(playerslist))

    print(players)

    tourneymaker()


    #hi_low()

#prints sheet id and range 
    # print("\n")
    # print(sheet_id + "\n")
    # print(rangename)

    
#for testing purposes just prints out object elo and name
    # for obj in playerslist:
    #     print(obj.Name, end =",")
    #     print(obj.Elo)


if __name__ == "__main__":
    main()