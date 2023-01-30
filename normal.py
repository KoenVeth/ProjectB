import requests
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
steamApiKey = "BBD242CD0468A435B14FB923B302231D"
steamID = "76561198351674547"

slink3 = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key="
slink4 = "&steamid=" + steamID + "&include_appinfo=1&format=json"
slink5 = slink3 + steamApiKey + slink4

r2 = requests.get(slink5)
friendslist = []
steam2 = r2.json()
lenfriend = steam2["friendslist"]["friends"]
lenghtfriend = len(lenfriend)
for i in range(0, lenghtfriend):
    friend = steam2["friendslist"]["friends"][i]["steamid"]
    # print(friend)
    friendslist.append(friend)
# Steam API link formatting for "GetOwnedGames"
game_count_list = []
for j in range(0, lenghtfriend):

    slink6 = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
    slink7 = "&steamid=" + friendslist[j] + "&include_appinfo=1&format=json"
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


game_count_list.sort()

mean= sum(game_count_list) // len(game_count_list)

newlist = []
numberlist=[]
# haal elk punt van het gemiddelde af
for i in range(0, len(game_count_list)):
    a = game_count_list[i] - mean
    # kwadrateer dat
    a = a ** 2
    newlist.append(a)
    # sommeer al die kwadraten
sum_a = sum(newlist)
    # deel dat door het aantal orginele getallen
res = sum_a / len(game_count_list)
sd=res**0.5
x_axis = np.arange(game_count_list[0], game_count_list[-1], 1)
plt.plot(x_axis, norm.pdf(x_axis, mean,sd))
plt.xlabel("aantal games")
plt.ylabel("kansverdeling")
plt.show()