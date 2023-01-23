import requests
import random
import datetime

steamApiKey = "BBD242CD0468A435B14FB923B302231D"
steamID = "76561198351674547"

slink3 = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key="
slink4 = "&steamid=" + steamID + "&include_appinfo=1&format=json"
slink5 = slink3 + steamApiKey + slink4

r2 = requests.get(slink5)
friendslist=[]
steam2 = r2.json()
lenfriend=steam2["friendslist"]["friends"]
lenghtfriend=len(lenfriend)
for i in range(0,lenghtfriend):
    friend=steam2["friendslist"]["friends"][i]["steamid"]
    #print(friend)
    friendslist.append(friend)
# Steam API link formatting for "GetOwnedGames"
for j in range(0,lenghtfriend):
    slink6 = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
    slink7 = "&steamid=" + friendslist[j] + "&include_appinfo=1&format=json"
    slink8 = slink6 + steamApiKey + slink7
    r = requests.get(slink8)

    # convert to JSON and save to another variable
    steam3 = r.json()
    weeks=steam3["response"]
    #print(steam3)
    print(weeks)
lastseenlist=[]
onlinelist=""
names=""
for j in range(0,lenghtfriend):
    slink1 = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="
    slink2 = "&steamids=" + friendslist[j] + "&include_appinfo=1&format=json"
    slink = slink1 + steamApiKey + slink2

    # Sent API Get request and save respond to a variable
    r = requests.get(slink)

    # convert to JSON and save to another variable
    steam = r.json()
    online = steam["response"]["players"][0]["personastate"]
    if online==0:
        onlinelist+="Offline,"
    elif online==1:
        onlinelist+="Online,"
    elif online==2:
        onlinelist+="Busy,"
    elif online== 3:
        onlinelist+="Away,"
    elif online== 4:
        onlinelist+="Snooze,"
    elif online == 5:
        onlinelist+= "Looking to trade,"
    elif online == 6:
        onlinelist+="Looking to play,"
    name = steam["response"]["players"][0]["personaname"]
    names+=name+","
    lastseen=steam["response"]["players"][0]["lastlogoff"]
    dt_utc_naive = datetime.datetime.utcfromtimestamp(lastseen)
    lasttime=dt_utc_naive.strftime(" %H:%M:%S %d-%m-%Y")
    lastseenlist.append(lasttime)

    # JSON output with information about each game owned
    #print(steam)
    # https://developer.valvesoftware.com/wiki/Steam_Web_API#GetOwnedGames_.28v0001.29
onlinelist=onlinelist.split(",")
onlinelist.pop(-1)
names=names.split(",")
names.pop(-1)
#print(lastseenlist)
#print(onlinelist)
#print(names)
