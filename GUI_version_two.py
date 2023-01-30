from customtkinter import *
import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image
import datetime
import requests
import json
import operator
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.stats import norm
import numpy as np

print("Loading.....\n")

# __________________________ Window settings __________________________ #
window = CTk()
window.title("Steam")
cycle = customtkinter.set_appearance_mode("dark")
window.geometry("900x650")
window.minsize(900, 650)
window.maxsize(900, 650)
steam_icon = PhotoImage(file="Steam_window_logo.png")
window.iconphoto(False, steam_icon)

# __________________________ API call __________________________ #
steamApiKey = "BBD242CD0468A435B14FB923B302231D"
steamID = "76561198351674547"

# "76561198351674547"
slink3 = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key="
slink4 = "&steamid=" + steamID + "&include_appinfo=1&format=json"
slink5 = slink3 + steamApiKey + slink4

r2 = requests.get(slink5)
print("Gathering friends list.")
friends_list = []
steam2 = r2.json()
len_friend = steam2["friendslist"]["friends"]
length_friend = len(len_friend)
for i in range(0, length_friend):
    friend = steam2["friendslist"]["friends"][i]["steamid"]

    friends_list.append(friend)
# Steam API link formatting for "GetOwnedGames"
print("Done!\n")

print("Gathering friend statistics.")
game_count_list = []
games_list = ""
for j in range(0, length_friend):

    slink6 = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
    slink7 = "&steamid=" + friends_list[j] + "&include_appinfo=1&format=json&include_played_free_games"
    slink8 = slink6 + steamApiKey + slink7
    r = requests.get(slink8)

    # convert to JSON and save to another variable
    steam3 = r.json()
    if steam3 == {'response': {}}:
        game_count_list.append(0)
        continue
    choice = random.choice(range(0, len(steam3["response"]["games"]) - 1))
    random_game = steam3["response"]["games"][choice]["name"]
    if random_game not in games_list:
        games_list += random_game + ";"
    games = steam3["response"]["game_count"]
    game_count_list.append(games)

games_list = games_list.split(";")
games_list.pop(-1)
print("Done!\n")

print("Gathering friends data.")
last_seen_list = []
online_list = ""
names = ""
for j in range(0, length_friend):
    slink1 = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="
    slink2 = "&steamids=" + friends_list[j] + "&include_appinfo=1&format=json"
    slink = slink1 + steamApiKey + slink2

    # Sent API Get request and save respond to a variable
    r = requests.get(slink)

    # conv ert to JSON and save to another variable
    steam = r.json()
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

online_list = online_list.split(",")
online_list.pop(-1)
names = names.split(",")
names.pop(-1)
friends_online = []
for k in range(0, length_friend):
    if online_list[k] == "Online     ✔":
        friends_online.append(names[k])
print("Done!\n")

print("Loading your friends play page.")

occurrence = []
total_playtime_list = []
for j in range(0, length_friend):

    slink9 = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
    slink10 = "&steamid=" + friends_list[j] + "&include_appinfo=1&format=json&include_played_free_games"
    slink11 = slink9 + steamApiKey + slink10
    r = requests.get(slink11)
    playtime_player = []

    steam4 = r.json()

    # if somebody has no games skip them
    # get a player's playtime for every game and add it to a list
    # add up the play times and add that to a total playtime list
    # get the most played game's index
    # if it's not a duplicate add it to the pl
    if steam4 == {'response': {}}:
        continue
    for s in range(0, len(steam4['response']['games']) - 1):
        playtime = steam4['response']['games'][s]['playtime_forever']
        playtime_player.append(playtime)
    total_playtime = sum(playtime_player) // 60
    total_playtime_list.append(total_playtime)
    max_playtime = max(playtime_player)
    max_index = playtime_player.index(max_playtime)
    most_played = steam4['response']['games'][max_index]['name']
    occurrence.append(most_played)

count_dict = {}
for u in range(0, len(occurrence) - 1):
    count_dict[occurrence[u]] = occurrence.count(occurrence[u])
top5 = {}
for k in sorted(count_dict, key=count_dict.get, reverse=True):
    count_one = count_dict[k]
    if len(top5) < 5:
        top5[k] = count_one
top5_games = list(top5.keys())
print("Done!\n")

print("All done!")
# __________________________ Functions __________________________ #
mode_switch_count = 1


average = round(sum(game_count_list) / len(game_count_list), 2)
range_lst = max(game_count_list) - min(game_count_list)

average2 = round(sum(total_playtime_list) / len(total_playtime_list), 2)
range_lst2 = max(total_playtime_list) - min(total_playtime_list)

def freq(lst):
    # First I make an empty dictionary
    # Then I set the keys to the integers in the list and set the default value to 0.
    # Right after I add 1 to the right(juiste) value using a for loop.
    # Example [1, 2, 3, 3, 2] turns into dict {1: 1, 2: 2, 3: 2}
    freq_dict = {}
    for num in lst:
        freq_dict.setdefault(num, 0)
        freq_dict[num] += 1
    return freq_dict


def modes(lst):
    # I start with an empty dictionary, And use my freq function.
    # Set the keys equal to the numbers in the lst and the value to 0.
    # Then everytime a number that occurs multiple times in the lst gets looped through, 1 will be added to the value
    # of that key.
    num_freq = {}
    for num in lst:
        num_freq.setdefault(num, 0)
        num_freq[num] += 1
    # Then ones I have the freq dict, I check to see what the highest value in the dict is.
    # I create an empty list called modi, and loop through the dict to see which value(freq) is equal to max_freq.
    # If the dict value(freq) is equal to max_freq(the highest freq) I append it to the list called modi.
    # I return a sorted modi list.
    max_freq = max(num_freq.values())
    modi = []
    for num, freq in num_freq.items():
        if freq == max_freq:
            modi.append(num)
    if len(lst) == len(modi):
        return "No modi"
    return sorted(modi)


def median(lst):
    # First I sort the given list.
    sorted_list = sorted(lst)
    # If the list is even, I then take the two middle numbers and divide them by two to get the median.
    if len(lst) % 2 == 0:
        first_median = sorted_list[len(sorted_list) // 2]
        second_median = sorted_list[len(sorted_list) // 2 - 1]
        median_answer = float((first_median + second_median) / 2)
        return median_answer
    # If the list is odd, then I just take the middle number and return it, because that's the median.
    else:
        median_answer = float(sorted_list[len(sorted_list) // 2])
        return median_answer


def var(lst):
    # first I get the average of the given list.
    average_number = sum(lst) / len(lst)
    # I make an empty list, so I can append the deviance from the list average for each number.
    var_list = []
    for num in lst:
        var_deviance = num - average_number
        var_list.append(var_deviance)
    # I make an empty list, so I can square each number of the var_list and append it to my new list.
    var_list_squared = []
    for num in var_list:
        squared = num ** 2
        var_list_squared.append(squared)
    # After that's done, I calculate the average of the var_list_squared and return it.
    sum_vlq = sum(var_list_squared)
    length_vlq = len(var_list_squared)
    average_squared_deviance = sum_vlq / length_vlq
    return round(average_squared_deviance, 2)


def std(lst):
    # To get the standerd deviance (standaardafwijking) I take the variantie and take the root of that number.
    standerd_deviance = var(lst) ** 0.5
    return round(standerd_deviance, 2)


def destroy():
    for widget in window.winfo_children():
        widget.destroy()


def home_screen():
    destroy()
    window.title("Steam Dashboard")
    button_color = "#173b6c"
    button_hover_color = "#156598"

    frame_1_home = CTkFrame(window, width=200, height=505, corner_radius=20)
    frame_1_home.place(x=10, y=125)

    frame_2_home = CTkFrame(window, width=880, height=100, corner_radius=20)
    frame_2_home.place(x=10, y=10)

    frame_3_home = CTkFrame(window, width=670, height=505, corner_radius=10)
    frame_3_home.place(x=220, y=125)

    textbox_1_home = CTkTextbox(frame_3_home, width=600, height=450, corner_radius=10, fg_color="#1D1E1E",
                                font=("italic", 15),  text_color="white")
    textbox_1_home.place(x=35, y=27.5)

    steam_logo_img_home = customtkinter.CTkImage(dark_image=Image.open("SteamLogo.png"), size=(64, 64))
    steam_logo_label_home = CTkLabel(frame_2_home, text="", image=steam_logo_img_home)
    steam_logo_label_home.place(x=20, y=15)

    steam_text_home = CTkLabel(frame_2_home, text="Steam     ", font=("italic", 30, "bold", "underline"))
    steam_text_home.place(x=110, y=35)

    # Buttons
    button_4_home = CTkButton(frame_1_home, text="Your friends play", width=165, height=150, corner_radius=20,
                              fg_color=button_color, hover_color=button_hover_color, font=("italic", 15, "bold"),
                              text_color="white", command=clicked_yfp)
    button_4_home.place(x=20, y=50)

    button_5_home = CTkButton(frame_1_home, text="Friends list", width=165, height=150, corner_radius=20,
                              fg_color=button_color, hover_color=button_hover_color, font=("italic", 15, "bold"),
                              text_color="white", command=clicked_fiend_list)
    button_5_home.place(x=20, y=210)

    button_6_home = CTkButton(frame_2_home, text="search", fg_color=button_c, hover_color=button_hc, width=90,
                              height=55, font=("italic", 15, "bold"), command=lambda: call2())
    button_6_home.place(x=700, y=20)
    # Labels
    label_2_home = CTkLabel(frame_1_home, text="Statistics", font=("italic", 15, "bold"))
    label_2_home.place(x=30, y=20)
    image = customtkinter.CTkImage(dark_image=Image.open("search-interface-symbol.png"), size=(30, 30))
    label_3_home = CTkLabel(frame_2_home, text="", image=image)
    label_3_home.place(x=655, y=35)

    image2 = customtkinter.CTkImage(dark_image=Image.open("valve.png"), size=(64, 64))
    label_4_home = CTkLabel(frame_1_home, text="", image=image2)
    label_4_home.place(x=120, y=440)

    # Entry & switch
    entry_1_home = CTkEntry(frame_2_home, width=350, height=60, corner_radius=20, border_color="")
    entry_1_home.place(x=300, y=20)

    switch_home = CTkSwitch(frame_2_home, text="", switch_width=40, switch_height=15, fg_color="white",
                            progress_color="#242424", command=cycle_change)
    switch_home.place(x=830, y=65)

    def binary_search_algorithm2(data, min, max, game2):
        # The json file gets sorted.
        # The binary search algorthm searched for the first and the last indexes in the data.
        # If the middle game matched with the input, it will return its index,
        # otherwise the algorithm searches in the higher or lower indexes.
        # It will repeat this process until the game is found.
        # If the game isn't found, the function will return -1.

        if max >= min:
            mid = (max + min) // 2
            if data[mid]["name"] == game2:
                return mid
            elif data[mid]["name"] > game2:
                return binary_search_algorithm2(data, min, mid - 1, game2)
            else:
                return binary_search_algorithm2(data, mid + 1, max, game2)
        else:
            return -1

    def call2():
        textbox_1_home.delete(0.0, END)
        game2 = entry_1_home.get()
        result2 = binary_search_algorithm2(data, 0, len(data) - 1, game2)

        # If the game is found, the data will be divided using the found game's index.
        # If -1 has been returned from the binary search algorithm, an error message will be displayed.
        # The data will be inserted into textbox_data2.

        if result2 != -1:
            appid = data[result2]["appid"]
            name = data[result2]["name"]
            release_date = data[result2]["release_date"]
            english = data[result2]["english"]
            if english == 0:
                english = "No"
            else:
                english = "Yes"
            developer = data[result2]["developer"]
            publisher = data[result2]["publisher"]
            platforms = data[result2]["platforms"]
            required_age = data[result2]["required_age"]
            categories = data[result2]["categories"]
            genres = data[result2]["genres"]
            steamspy_tags = data[result2]['steamspy_tags']
            achievements = data[result2]['achievements']
            postive_ratings = data[result2]['positive_ratings']
            negative_ratings = data[result2]['negative_ratings']
            average_playtime = data[result2]['average_playtime']
            median_playtime = data[result2]['median_playtime']
            owners = data[result2]['owners']
            price = data[result2]['price']

            textbox_data2 = f"App ID: {appid}\n\nName: {name}\n\nDeveloper: {developer}\n\n" \
                           f"Release date: {release_date}\n\nPublisher: {publisher}\n\nPlatforms: {platforms}\n\n" \
                           f"Price: $ {price}\n\nRequired age: {required_age}\n\nCategories: {categories}\n\n" \
                           f"Genres: {genres}\n\nSteamspy_tags: {steamspy_tags}\n\nAchievements: {achievements}\n\n" \
                           f"Positive ratings: {postive_ratings}\n\nNegative_ratings: {negative_ratings}\n\n" \
                           f"Average playtime: {average_playtime} hours\n\nMedian playtime: {median_playtime} hours\n\n" \
                           f"Owners: {owners}\n\nAvailable in English: {english}"
            textbox_1_home.insert(0.0, textbox_data2)
        else:
            messagebox.showinfo("Error",
                                "Make sure the game has been spelled correctly.\nNote: This database has no game past 2019\nAnd the game has to be on Steam.")


def clicked_fiend_list():
    destroy()
    window.title("Friends list")

    textbox1 = CTkTextbox(window, width=825, height=500, font=("italic", 20), fg_color="#1D1E1E", text_color="white")
    textbox1.place(x=37.5, y=100)

    # I make an empty string and set Counter1 equal to 1.
    # Then I use a forloop to loop through each item in the three lists, and add it to the string in the form of
    # f strings sot that it is nicely formatted. With each loop Counter1 increases by one.
    # At the end of the forloop I insert the string to textbox1.

    name_str = ""
    counter1 = 1
    for name, status, log in zip(names, online_list, last_seen_list):
        name_str += f"{counter1}: {name} "
        name_str += "\t\t\t   "
        name_str += f"{status}"
        name_str += "\t\t\t     "
        name_str += f"{log}"
        name_str += "\n\n"
        counter1 += 1
    textbox1.insert(0.0, name_str)

    label1 = CTkLabel(window, text="Friends list.", font=("italic", 45, "bold"))
    label1.place(x=37.5, y=20)

    label2 = CTkLabel(window, text="Gamertag", font=("italic", 20, "bold"))
    label2.place(x=37.5, y=72)

    label3 = CTkLabel(window, text="Status", font=("italic", 20, "bold"))
    label3.place(x=325, y=72)

    label4 = CTkLabel(window, text="Last log-off", font=("italic", 20, "bold"))
    label4.place(x=612.5, y=72)

    button1 = CTkButton(window, text="Home", width=250, height=50, fg_color="#173b6c",
                        hover_color="#1D1E1E", font=("italic", 17, "bold"), command=home_screen)
    button1.place(x=612.5, y=10)

    button2 = CTkButton(window, text="Friend's gaming data", fg_color="#173b6c", hover_color="#1D1E1E",
                        height=50, width=250, font=("italic", 14, "bold"), command=clicked_gaming_data)
    button2.place(x=325, y=10)


def clicked_gaming_data():
    global average, range_lst
    destroy()
    window.title("Friend's play time data")
    frame1 = CTkFrame(window, width=350, height=610, fg_color="#1D1E1E")
    frame1.place(x=530, y=20)

    fig = plt.Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)

    x = len(total_playtime_list)

    x_list = []
    y_list = []
    for n in range(0, x):
        x_list.append(n)
        y = total_playtime_list[n]
        y_list.append(y)

    ax.bar(x_list, y_list)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    canvas.get_tk_widget().place(x=25, y=75)

    # The game data tab shows the user statistics about the game count of their friends list.
    # Such as: How many games do my friends have on average. Or how many friends have the same amount of games.
    # The code uses functions named: average, range_lst, median, var, modes, std to find out the statistics of the
    # friends game data. Then the code adds the return value to an f string.

    label_one = CTkLabel(frame1, text=f"Average: {average2}", font=("italic", 22, "bold"), text_color="white")
    label_one.place(x=20, y=20)

    label_two = CTkLabel(frame1, text=f"Range: {range_lst2}", font=("italic", 22, "bold"), text_color="white")
    label_two.place(x=20, y=80)

    label_three = CTkLabel(frame1, text=f"Median: {median(total_playtime_list)}", font=("italic", 22, "bold"), text_color="white")
    label_three.place(x=20, y=140)

    label_four = CTkLabel(frame1, text=f"Variance: {var(total_playtime_list)}", font=("italic", 22, "bold"), text_color="white")
    label_four.place(x=20, y=200)

    label_five = CTkLabel(frame1, text=f"Modes: {modes(total_playtime_list)}", font=("italic", 22, "bold"), text_color="white")
    label_five.place(x=20, y=260)

    label_six = CTkLabel(frame1, text=f"Standard deviance: {std(total_playtime_list)}", font=("italic", 22, "bold"), text_color="white")
    label_six.place(x=20, y=320)

    label_eight = CTkLabel(window, text="Friend's play time data", font=("italic", 30, "bold"))
    label_eight.place(x=25, y=10)

    button_one = CTkButton(frame1, text="Back", width=80, height=50, fg_color="#173b6c",
                           hover_color="#1D1E1E", font=("italic", 17, "bold"), command=clicked_fiend_list)
    button_one.place(x=260, y=550)

    button_two = CTkButton(window, text="Next", width=80, height=50, fg_color="#173b6c",
                           hover_color="#1D1E1E", font=("italic", 17, "bold"), command=clicked_gaming_data2)
    button_two.place(x=400, y=10)

    img1 = customtkinter.CTkImage(dark_image=Image.open("data-analysis.png"), size=(150, 150))
    label_seven = CTkLabel(frame1, text="", image=img1)
    label_seven.place(x=20, y=400)

    # Here the code checks to see if the average is 0. If that's the case, then that means that the API is down.
    # If the API is down, then a label will be made saying "API down".
    # The API has gone down multiple times during development of this project.

    if average == 0:
        destroy()
        error_label = CTkLabel(window, text="Error, API down!", font=("italic", 30, "bold"))
        error_label.place(x=335, y=280)

        messagebox.showinfo("Error", "One of the Steam API' has gone down.\nPlease come back later.")

        button_1_error = CTkButton(window, width=200, height=70, text="Home", font=("italic", 17, "bold"),
                                     fg_color="#173b6c", hover_color="#1D1E1E", command=home_screen)
        button_1_error.place(x=350, y=330)


def clicked_gaming_data2():
    destroy()
    window.title("Friend's game ownership data")



    game_count_list.sort()
    mean = sum(game_count_list) // len(game_count_list)

    new_list = []
    # haal elk punt van het gemiddelde af
    for i in range(0, len(game_count_list)):
        a = game_count_list[i] - mean
        # kwadrateer dat
        a = a ** 2
        new_list.append(a)
        # sommeer al die kwadraten
    sum_a = sum(new_list)
    # deel dat door het aantal orginele getallen
    res = sum_a / len(game_count_list)
    sd = res ** 0.5

    x_axis = np.arange(game_count_list[0], game_count_list[-1], 1)
    plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
    plt.xlabel("aantal games")
    plt.ylabel("kansverdeling")

    fig = plt.Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)

    ax.plot(x_axis, norm.pdf(x_axis, mean, sd))
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    canvas.get_tk_widget().place(x=25, y=75)


    # The game data tab shows the user statistics about the game count of their friends list.
    # Such as: How many games do my friends have on average. Or how many friends have the same amount of games.
    # The code uses functions named: average, range_lst, median, var, modes, std to find out the statistics of the
    # friends game data. Then the code adds the return value to an f string.

    frame1 = CTkFrame(window, width=350, height=610, fg_color="#1D1E1E")
    frame1.place(x=530, y=20)

    label_one = CTkLabel(frame1, text=f"Average: {average}", font=("italic", 22, "bold"), text_color="white")
    label_one.place(x=20, y=20)

    label_two = CTkLabel(frame1, text=f"Range: {range_lst}", font=("italic", 22, "bold"), text_color="white")
    label_two.place(x=20, y=80)

    label_three = CTkLabel(frame1, text=f"Median: {median(game_count_list)}", font=("italic", 22, "bold"),
                           text_color="white")
    label_three.place(x=20, y=140)

    label_four = CTkLabel(frame1, text=f"Variance: {var(game_count_list)}", font=("italic", 22, "bold"),
                          text_color="white")
    label_four.place(x=20, y=200)

    label_five = CTkLabel(frame1, text=f"Modes: {modes(game_count_list)}", font=("italic", 22, "bold"),
                          text_color="white")
    label_five.place(x=20, y=260)

    label_six = CTkLabel(frame1, text=f"Standard deviance: {std(game_count_list)}", font=("italic", 22, "bold"),
                         text_color="white")
    label_six.place(x=20, y=320)

    label_eight2 = CTkLabel(window, text="Friend's game count data", font=("italic", 30, "bold"))
    label_eight2.place(x=25, y=10)

    button_one = CTkButton(frame1, text="Previous", width=80, height=50, fg_color="#173b6c",
                           hover_color="#1D1E1E", font=("italic", 17, "bold"), command=clicked_gaming_data)
    button_one.place(x=260, y=550)

    img1 = customtkinter.CTkImage(dark_image=Image.open("data-analysis.png"), size=(150, 150))
    label_seven = CTkLabel(frame1, text="", image=img1)
    label_seven.place(x=20, y=400)

    # Here the code checks to see if the average is 0. If that's the case, then that means that the API is down.
    # If the API is down, then a label will be made saying "API down".
    # The API has gone down multiple times during development of this project.

    if average == 0:
        destroy()
        error_label = CTkLabel(window, text="Error, API down!", font=("italic", 30, "bold"))
        error_label.place(x=335, y=280)

        messagebox.showinfo("Error", "One of the Steam API' has gone down.\nPlease come back later.")

        button_1_error = CTkButton(window, width=200, height=70, text="Home", font=("italic", 17, "bold"),
                                     fg_color="#173b6c", hover_color="#1D1E1E", command=home_screen)
        button_1_error.place(x=350, y=330)


def clicked_yfp():
    destroy()
    window.title("Your friends play")
    frame_1_friends = CTkFrame(window, width=650, height=125, corner_radius=10)
    frame_1_friends.place(x=10, y=10)

    frame_2_friends = CTkFrame(window, width=220, height=620, corner_radius=10)
    frame_2_friends.place(x=670, y=10)

    img_1_friends = customtkinter.CTkImage(dark_image=Image.open("team.png"), size=(100, 100))
    label_1_friends = CTkLabel(frame_2_friends, text="", image=img_1_friends)
    label_1_friends.place(x=60, y=500)

    label_2_friends = CTkLabel(window, text="Games your friends play", font=("Italic", 25, "bold"))
    label_2_friends.place(x=15, y=150)

    img_2_friends = customtkinter.CTkImage(dark_image=Image.open("steam_baner-modified.png"), size=(250, 100))
    label_3_friends = CTkLabel(frame_1_friends, text="", image=img_2_friends)
    label_3_friends.place(x=75, y=10)

    label_3_friends = CTkLabel(frame_2_friends, text="Online right now!", font=("italic", 20, "bold"))
    label_3_friends.place(x=15, y=160)

    img_3_friends = customtkinter.CTkImage(dark_image=Image.open("valve (1).png"), size=(250, 125))
    label_4_friends = CTkLabel(frame_1_friends, text="", image=img_3_friends)
    label_4_friends.place(x=350, y=0)

    label_5_friends = CTkLabel(window, text="Most played games", font=("Italic", 25, "bold"))
    label_5_friends.place(x=345, y=152)

    textbox_1_friends = CTkTextbox(window, width=320, height=430, corner_radius=10, text_color="white",
                                   fg_color="#1D1E1E", font=("italic", 15))
    textbox_1_friends.place(x=10, y=200)

    # An empty string has been made. Then a forloop loops through every game in the list, and dds it to te empty string
    # in the form of an f string. At the end the string will be inserted to textbox_1_friends.

    textbox_1_friends_str = ""
    for g in games_list:
        textbox_1_friends_str += f"{g}\n\n"
    textbox_1_friends.insert(0.0, textbox_1_friends_str)

    textbox_2_friends = CTkTextbox(window, width=320, height=430, corner_radius=10, text_color="white",
                                   fg_color="#1D1E1E", font=("italic", 18))
    textbox_2_friends.place(x=340, y=200)

    # An empty string has been made. Then a forloop loops through every game in the list, and dds it to te empty string
    # in the form of an f string. At the end the string will be inserted to textbox_2_friends.

    textbox_2_friends_str = ""
    for n in top5_games:
        textbox_2_friends_str += f"{n}\n\n\n"
    textbox_2_friends.insert(0.0, textbox_2_friends_str)

    textbox_3_friends = CTkTextbox(frame_2_friends, width=200, height=300, corner_radius=10, text_color="white",
                                   fg_color="#1D1E1E", font=("italic", 20))
    textbox_3_friends.place(x=10, y=190)

    # An empty string has been made. Then a forloop loops through every friend in the list, and dds it to te empty
    # string in the form of an f string. At the end the string will be inserted to textbox_3_friends.

    textbox_3_friends_str = ""
    for n in friends_online:
        textbox_3_friends_str += f"{n}\n\n"
    textbox_3_friends.insert(0.0, textbox_3_friends_str)

    button_1_friends = CTkButton(frame_2_friends, width=200, height=70, text="Home", font=("italic", 17, "bold"),
                                 fg_color="#173b6c", hover_color="#1D1E1E", command=home_screen)
    button_1_friends.place(x=10, y=30)


def cycle_change():
    global cycle, mode_switch_count, button_c, button_hc
    mode_switch_count += 1
    if mode_switch_count % 2:
        cycle = customtkinter.set_appearance_mode("dark")
    else:
        cycle = customtkinter.set_appearance_mode("light")


# __________________________ Widgets __________________________ #
# Button colors
button_c = "#173b6c"
button_hc = "#156598"


frame_1 = CTkFrame(window, width=200, height=505, corner_radius=10)
frame_1.place(x=10, y=125)

frame_2 = CTkFrame(window, width=880, height=100, corner_radius=10)
frame_2.place(x=10, y=10)

frame_3 = CTkFrame(window, width=670, height=505, corner_radius=10)
frame_3.place(x=220, y=125)

textbox_1 = CTkTextbox(frame_3, width=600, height=450, corner_radius=10, fg_color="#1D1E1E", font=("italic", 15),
                       text_color="white")
textbox_1.place(x=35, y=27.5)

steam_logo_img = customtkinter.CTkImage(dark_image=Image.open("SteamLogo.png"), size=(64, 64))
steam_logo_label = CTkLabel(frame_2, text="", image=steam_logo_img)
steam_logo_label.place(x=20, y=15)

steam_text = CTkLabel(frame_2, text="Steam  ", font=("italic", 30, "bold", "underline"))
steam_text.place(x=110, y=35)

# Buttons
button_4 = CTkButton(frame_1, text="Your friends play", width=165, height=150, corner_radius=20,
                     fg_color=button_c, hover_color=button_hc, font=("italic", 15, "bold"), command=clicked_yfp)
button_4.place(x=20, y=50)

button_5 = CTkButton(frame_1, text="Friends list", width=165, height=150, corner_radius=20,
                     fg_color=button_c, hover_color=button_hc, font=("italic", 15, "bold"), command=clicked_fiend_list)
button_5.place(x=20, y=210)

# Labels
label_2 = CTkLabel(frame_1, text="Statistics", font=("italic", 15, "bold"))
label_2.place(x=30, y=20)

img = customtkinter.CTkImage(dark_image=Image.open("search-interface-symbol.png"), size=(30, 30))
label_3 = CTkLabel(frame_2, text="", image=img)
label_3.place(x=655, y=35)


img2 = customtkinter.CTkImage(dark_image=Image.open("valve.png"), size=(64, 64))
label_4 = CTkLabel(frame_1, text="", image=img2)
label_4.place(x=120, y=440)

# Entry & switch
entry_1 = CTkEntry(frame_2, width=350, height=60, corner_radius=20, border_color="")
entry_1.place(x=300, y=20)

switch = CTkSwitch(frame_2, text="", switch_width=40, switch_height=15, fg_color="white",
                   progress_color="#242424", command=cycle_change)
switch.place(x=830, y=65)

j = open("steam.json")  # open json
data = json.load(j)  # load the data
data.sort(key=operator.itemgetter('name'))  # sort the games by name


def binary_search_algorithm(data, min, max, game):
    # The json file gets sorted.
    # The binary search algorthm searched for the first and the last indexes in the data.
    # If the middle game matched with the input, it will return its index,
    # otherwise the algorithm searches in the higher or lower indexes.
    # It will repeat this process until the game is found.
    # If the game isn't found, the function will return -1.

    if max >= min:
        mid = (max + min) // 2
        if data[mid]["name"] == game:
            return mid
        elif data[mid]["name"] > game:
            return binary_search_algorithm(data, min, mid - 1, game)
        else:
            return binary_search_algorithm(data, mid + 1, max, game)
    else:
        return -1


def call():
    textbox_1.delete(0.0, END)
    game = entry_1.get()
    result = binary_search_algorithm(data, 0, len(data) - 1, game)

    # If the game is found, the data will be divided using the found game's index.
    # If -1 has been returned from the binary search algorithm, an error message will be displayed.
    # The data will be inserted into textbox_data.

    if result != -1:
        appid = data[result]["appid"]
        name = data[result]["name"]
        release_date = data[result]["release_date"]
        english = data[result]["english"]
        if english == 0:
            english = "No"
        else:
            english = "Yes"
        developer = data[result]["developer"]
        publisher = data[result]["publisher"]
        platforms = data[result]["platforms"]
        required_age = data[result]["required_age"]
        categories = data[result]["categories"]
        genres = data[result]["genres"]
        steamspy_tags = data[result]['steamspy_tags']
        achievements = data[result]['achievements']
        postive_ratings = data[result]['positive_ratings']
        negative_ratings = data[result]['negative_ratings']
        average_playtime = data[result]['average_playtime']
        median_playtime = data[result]['median_playtime']
        owners = data[result]['owners']
        price = data[result]['price']
        textbox_data = f"App ID: {appid}\n\nName: {name}\n\nDeveloper: {developer}\n\n" \
                       f"Release date: {release_date}\n\nPublisher: {publisher}\n\nPlatforms: {platforms}\n\n" \
                       f"Price: $ {price}\n\nRequired age: {required_age}\n\nCategories: {categories}\n\n" \
                       f"Genres: {genres}\n\nSteamspy_tags: {steamspy_tags}\n\nAchievements: {achievements}\n\n" \
                       f"Positive ratings: {postive_ratings}\n\nNegative_ratings: {negative_ratings}\n\n" \
                       f"Average playtime: {average_playtime} hours\n\nMedian playtime: {median_playtime} hours\n\n" \
                       f"Owners: {owners}\n\nAvailable in English: {english}"
        textbox_1.insert(0.0, textbox_data)
    else:
        messagebox.showinfo("Error", "Make sure the game has been spelled correctly.\nNote: This database has no game past 2019\nAnd the game has to be on Steam.")


button_6 = CTkButton(frame_2, text="search", fg_color=button_c, hover_color=button_hc, width=90, height=55,
                     font=("italic", 15, "bold"), command=lambda: call())
button_6.place(x=700, y=22)

window.mainloop()
