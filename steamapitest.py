import requests
import random
import datetime
import json

#steamApiKey="AAFB2DC04D5E96CD98660900ADC52FAC"
steamApiKey = "BBD242CD0468A435B14FB923B302231D"
#steamID="76561198978002270"#p
steamID = "76561198351674547"#i

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
gameslist=""
for j in range(0, length_friend):

    slink6 = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
    slink7 = "&steamid=" + friends_list[j] + "&include_appinfo=1&format=json"
    slink8 = slink6 + steamApiKey + slink7
    r = requests.get(slink8)

    # convert to JSON and save to another variable
    steam3 = r.json()
    if steam3 == {'response': {}}:
        game_count_list.append(0)
        continue
    choice = random.choice(range(0, len(steam3["response"]["games"]) - 1))
    randomgame = steam3["response"]["games"][choice]["name"]
    if randomgame not in gameslist:
        gameslist+=randomgame+";"
    games = steam3["response"]["game_count"]
    game_count_list.append(games)
    #print(steam3)
#print(game_count_list)
#print(gameslist)

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
friends_online=[]
for k in range(0,length_friend):
    if online_list[k]=="Online":
        friends_online.append(names[k])
print(friends_online)
#print(lastseenlist)
#print(online_list)
#print(names)
#most played games
playlist=[]
for j in range(0, length_friend):

    slink9 = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
    slink10 = "&steamid=" + friends_list[j] + "&include_appinfo=1&format=json"
    slink11 = slink9 + steamApiKey + slink10
    r = requests.get(slink11)
    playlist_player=[]
    # convert to JSON and save to another variable
    steam4 = r.json()
    if steam4 == {'response': {}}:
        continue
    for s in range(0, len(steam4['response']['games'])-1):
       playtime= steam4['response']['games'][s]['playtime_forever']
       playlist_player.append(playtime)
    max_playtime=max(playlist_player)
    max_index=playlist_player.index(max_playtime)
    mostplayed=steam4['response']['games'][max_index]['name']
    if mostplayed not in playlist:
        playlist.append(mostplayed)

    #print(steam4)

print(playlist)
#top3 games
