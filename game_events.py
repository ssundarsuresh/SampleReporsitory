import sys
import datetime
import random
import math

def simulate():
        #Generates date for the last 30 days and save it in a list
        thedate=[]
        for i in range(1,30):
                thedate.append(datetime.date.today()-datetime.timedelta(days=i))
        #level is assumed to be between 1 and 40 and since assigned on a random basis this will no sync with event date for a user        
        level=[j for j in range(1,40)]
        #This is a master list for event names
        eventname=["GameLoad","GameStart","ClickBuy","ClickEnd","sendInvite","SendGift","BuyGold","Buy_XP","Gameend","ErrorLoad_ok","makeShipment","acceptGift","AcceptSurvey","build_farm","build_Temple","Build_Idol","clickRefresh"]
        UserID=[k for k in range(1,100)]

        f=open("game_events.tsv","w")
        for dt in thedate:
                for records in range(1000):
                        theday=dt
                        UID=random.choice(UserID)
                        atevent=random.choice(eventname)
                        atlevel=random.choice(level)
                        if      atevent=="sendInvite":
                                Gold=100
                        elif    atevent=="BuyGold":
                                Gold=1000
                        elif    atevent=="acceptGift":
                                Gold=250
                        else    :
                                Gold=""
                        if      atevent=="Buy_XP":
                                xp=1000
                        elif    atevent=="ClickBuy":
                                xp=3000
                        else    :
                                xp=""
                        f.writelines((str(theday) + '\t' + str(UID) + '\t' + atevent + '\t' + str(atlevel) + '\t' + str(Gold) + '\t' + str(xp) +'\n'))
        f.close()
def main():
        simulate()
