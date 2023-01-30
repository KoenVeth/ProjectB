import requests
import random
import datetime

# get your api key
# insert your SteamID
# Get the link to the API
# connect to the JSON-file and get it
steamApiKey = "BBD242CD0468A435B14FB923B302231D"
steamID = "76561198351674547"
slink3 = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key="
slink4 = "&steamid=" + steamID + "&include_appinfo=1&format=json"
slink5 = slink3 + steamApiKey + slink4
r2 = requests.get(slink5)
friends_list = []
steam2 = r2.json()

# determine the length of the friendslist
# get all steamIDs for the friends
friends = steam2["friendslist"]["friends"]
length_friend = len(friends)
for i in range(0, length_friend):
    friend = steam2["friendslist"]["friends"][i]["steamid"]
    friends_list.append(friend)

# use a for loop to get all data for the friends in the friends list
# Get the link to the next API
# connect to the JSON-file and get it
game_count_list = []
gameslist = ""
for j in range(0, length_friend):

    slink6 = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
    slink7 = "&steamid=" + friends_list[j] + "&include_appinfo=1&format=json&include_played_free_games"
    slink8 = slink6 + steamApiKey + slink7
    r = requests.get(slink8)
    steam3 = r.json()
    # if somebody has no games skip it
    # add the amount of games for every player to a list
    if steam3 == {'response': {}}:
        game_count_list.append(0)
        continue
    games = steam3["response"]["game_count"]
    game_count_list.append(games)

    # pick a random number between 0 and the index of the length of the games list
    # use that number to pick a random game and add that to the games list
    choice = random.choice(range(0, len(steam3["response"]["games"]) - 1))
    randomgame = steam3["response"]["games"][choice]["name"]
    if randomgame not in gameslist:
        gameslist += randomgame + ";"

# use a for loop to get all data for the friends in the friends list
# Get the link to the next API
# connect to the JSON-file and get it

last_seen_list = []
online_list = ""
names = ""
for j in range(0, length_friend):
    slink1 = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="
    slink2 = "&steamids=" + friends_list[j] + "&include_appinfo=1&format=json"
    slink = slink1 + steamApiKey + slink2
    r = requests.get(slink)
    steam = r.json()

    # get people's online status
    # convert the numbers to the text they represent
    # get their username and the date they were last online and convert it to CET
    online = steam["response"]["players"][0]["personastate"]
    if online == 0:
        online_list += "Offline     ❌,"
    elif online == 1:
        online_list += "Online     ✔,"
    elif online == 2:
        online_list += "Busy,"
    elif online == 3:
        online_list += "Away      👋,"
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
#split the strings at the comma to turn them into lists
#remove the empty space at the end
online_list = online_list.split(",")
online_list.pop(-1)
names = names.split(",")
names.pop(-1)
friends_online = []
for k in range(0, length_friend):
    if online_list[k] == "Online":
        friends_online.append(names[k])
# use a for loop to get all data for the friends in the friends list
# Get the link to the next API
# connect to the JSON-file and get it
playlist = []
occurrence = []
total_playtime_list=[]
for j in range(0, length_friend):

    slink9 = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
    slink10 = "&steamid=" + friends_list[j] + "&include_appinfo=1&format=json&include_played_free_games"
    slink11 = slink9 + steamApiKey + slink10
    r = requests.get(slink11)
    playtime_player = []

    steam4 = r.json()

    #if somebody has no games skip them
    # get a player's playtime for every game and add it to a list
    # add up the playtimes and add that to a total playtime list
    #get the most played game's index
    #add th emost played game to the occurance list
    if steam4 == {'response': {}}:
        continue
    for s in range(0, len(steam4['response']['games']) - 1):
        playtime = steam4['response']['games'][s]['playtime_forever']
        playtime_player.append(playtime)
    total_playtime = sum(playtime_player)
    total_playtime_list.append(total_playtime)
    max_playtime = max(playtime_player)
    max_index = playtime_player.index(max_playtime)
    mostplayed = steam4['response']['games'][max_index]['name']
    occurrence.append(mostplayed)

print(total_playtime_list)
#create a dictionary for the amount of times a game occures in a max list
#add and organize the occurances in that dictionary

countdict = {}
# print(steam4)
for u in range(0, len(occurrence) - 1):
    # print(occurrence.count(occurrence[u]))
    countdict[occurrence[u]] = occurrence.count(occurrence[u])
# print(countdict)

#sort the dict by amount of games
# add the top 5 to the new dictionary
#the keys are the games, put those in a new list
top3 = {}
for k in sorted(countdict, key=countdict.get, reverse=True):
    count_one = countdict[k]
    if len(top3) < 5:
        top3[k] = count_one
# print(top3)
top5_games = list(top3.keys())
print(top5_games)
