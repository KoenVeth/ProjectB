import requests
import random
import datetime

steamApiKey = "BBD242CD0468A435B14FB923B302231D"
steamID = "76561198351674547"

slink3 = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key="
slink4 = "&steamid=" + steamID + "&include_appinfo=1&format=json"
slink5 = slink3 + steamApiKey + slink4

r2 = requests.get(slink5)
friends_list = []
steam2 = r2.json()
len_friend = steam2["friendslist"]["friends"]
length_friend = len(len_friend)
for i in range(0, length_friend):
    friend = steam2["friendslist"]["friends"][i]["steamid"]
    # print(friend)
    friends_list.append(friend)
# Steam API link formatting for "GetOwnedGames"
game_count_list = []
for j in range(0, length_friend):

    slink6 = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
    slink7 = "&steamid=" + friends_list[j] + "&include_appinfo=1&format=json"
    slink8 = slink6 + steamApiKey + slink7
    r = requests.get(slink8)

    # convert to JSON and save to another variable

    steam3 = r.json()
    # weeks=steam3["response"]["games"]
    if steam3 == {'response': {}}:
        game_count_list.append(0)
        continue
    games = steam3["response"]["game_count"]
    game_count_list.append(games)
    # print(steam3)
print(game_count_list)

last_seen_list = []
online_list = ""
names = ""
for j in range(0, length_friend):
    slink1 = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="
    slink2 = "&steamids=" + friends_list[j] + "&include_appinfo=1&format=json"
    slink = slink1 + steamApiKey + slink2

    # Sent API Get request and save respond to a variable
    r = requests.get(slink)

    # convert to JSON and save to another variable
    steam = r.json()
    online = steam["response"]["players"][0]["personastate"]
    if online == 0:
        online_list += "Offline,"
    elif online == 1:
        online_list += "Online,"
    elif online == 2:
        online_list += "Busy,"
    elif online == 3:
        online_list += "Away,"
    elif online == 4:
        online_list += "Snooze,"
    elif online == 5:
        online_list += "Looking to trade,"
    elif online == 6:
        online_list += "Looking to play,"
    name = steam["response"]["players"][0]["personaname"]
    names += name + ","
    last_seen = steam["response"]["players"][0]["lastlogoff"]
    dt_utc_naive = datetime.datetime.utcfromtimestamp(last_seen)
    last_time = dt_utc_naive.strftime(" %H:%M:%S %d-%m-%Y")
    last_seen_list.append(last_time)

online_list = online_list.split(",")
online_list.pop(-1)
names = names.split(",")
names.pop(-1)
#print(lastseenlist)
#print(online_list)
#print(names)

