from customtkinter import *
import customtkinter
from tkinter import *
from PIL import Image
import datetime
import requests
import pytz
import json
import operator

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
    # print(friend)
    friends_list.append(friend)
# Steam API link formatting for "GetOwnedGames"
print("Done!\n")

print("Gathering friend statistics.")
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
    utc = dt_utc_naive.replace(tzinfo=pytz.utc)
    tz = pytz.timezone('Europe/Berlin')
    cet = utc.astimezone(tz)
    last_time = cet.strftime(" %H:%M  %d-%m-%Y")
    last_seen_list.append(last_time)

online_list = online_list.split(",")
online_list.pop(-1)
names = names.split(",")
names.pop(-1)
print("Done!\n")

print("All done!")
# __________________________ Functions __________________________ #
mode_switch_count = 1


average = round(sum(game_count_list) / len(game_count_list), 2)
range_lst = max(game_count_list) - min(game_count_list)


def freq(lst=game_count_list):
    # First I make an empty dictionary
    # Then I set the keys to the integers in the list and set the default value to 0.
    # Right after I add 1 to the right(juiste) value using a for loop.
    # Example [1, 2, 3, 3, 2] turns into dict {1: 1, 2: 2, 3: 2}
    freq_dict = {}
    for num in lst:
        freq_dict.setdefault(num, 0)
        freq_dict[num] += 1
    return freq_dict


def modes(lst=game_count_list):
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
    return sorted(modi)


def median(lst=game_count_list):
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


def var(lst=game_count_list):
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


def std(lst=game_count_list):
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

    textbox_1_home = CTkTextbox(frame_3_home, width=600, height=450, corner_radius=10, fg_color="#1D1E1E")
    textbox_1_home.place(x=35, y=27.5)

    steam_logo_img_home = customtkinter.CTkImage(dark_image=Image.open("SteamLogo.png"), size=(64, 64))
    steam_logo_label_home = CTkLabel(frame_2_home, text="", image=steam_logo_img_home)
    steam_logo_label_home.place(x=20, y=15)

    steam_text_home = CTkLabel(frame_2_home, text="Steam     ", font=("italic", 30, "bold", "underline"))
    steam_text_home.place(x=110, y=35)

    # Buttons
    button_4_home = CTkButton(frame_1_home, text="Your friends play", width=165, height=150, corner_radius=20,
                              fg_color=button_color, hover_color=button_hover_color, font=("italic", 15, "bold"),
                              text_color="white")
    button_4_home.place(x=20, y=50)

    button_5_home = CTkButton(frame_1_home, text="Friends list", width=165, height=150, corner_radius=20,
                              fg_color=button_color, hover_color=button_hover_color, font=("italic", 15, "bold"),
                              text_color="white", command=clicked_fiend_list)
    button_5_home.place(x=20, y=210)
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


def clicked_fiend_list():
    destroy()
    window.title("Friends list")

    textbox1 = CTkTextbox(window, width=250, height=500, font=("italic", 20), fg_color="#1D1E1E", text_color="white")
    textbox1.place(x=37.5, y=100)
    name_str = ""
    counter1 = 1
    for name in names:
        name_str += f"{counter1}: {name}\n\n"
        counter1 += 1
    textbox1.insert(0.0, name_str)

    textbox2 = CTkTextbox(window, width=250, height=500, font=("italic", 20), fg_color="#1D1E1E", text_color="white")
    textbox2.place(x=325, y=100)

    online_str = ""
    counter2 = 1
    for status in online_list:
        online_str += f"{counter2}: {status}\n\n"
        counter2 += 1
    textbox2.insert(0.0, online_str)

    textbox3 = CTkTextbox(window, width=250, height=500, font=("italic", 20), fg_color="#1D1E1E", text_color="white")
    textbox3.place(x=612.5, y=100)

    log_off = ""
    counter3 = 1
    for log in last_seen_list:
        log_off += f"{counter3}: {log}\n\n"
        counter3 += 1
    textbox3.insert(0.0, log_off)

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

    button2 = CTkButton(window, text="Friend's game ownership data", fg_color="#173b6c", hover_color="#1D1E1E",
                        height=50, width=250, font=("italic", 14, "bold"), command=clicked_game_data)
    button2.place(x=325, y=10)


def clicked_game_data():
    destroy()
    window.title("Friend's game ownership data")
    frame1 = CTkFrame(window, width=430, height=610, fg_color="#1D1E1E")
    frame1.place(x=450, y=20)

    label_one = CTkLabel(frame1, text=f"Average: {average}", font=("italic", 25, "bold"), text_color="white")
    label_one.place(x=20, y=20)

    label_two = CTkLabel(frame1, text=f"Range: {range_lst}", font=("italic", 25, "bold"), text_color="white")
    label_two.place(x=20, y=80)

    label_three = CTkLabel(frame1, text=f"Median: {median()}", font=("italic", 25, "bold"), text_color="white")
    label_three.place(x=20, y=140)

    label_four = CTkLabel(frame1, text=f"Variance: {var()}", font=("italic", 25, "bold"), text_color="white")
    label_four.place(x=20, y=200)

    label_five = CTkLabel(frame1, text=f"Modes: {modes()}", font=("italic", 25, "bold"), text_color="white")
    label_five.place(x=20, y=260)

    label_six = CTkLabel(frame1, text=f"Standard deviance: {std()}", font=("italic", 25, "bold"), text_color="white")
    label_six.place(x=20, y=320)

    button_one = CTkButton(frame1, text="Back", width=80, height=50, fg_color="#173b6c",
                           hover_color="#1D1E1E", font=("italic", 17, "bold"), command=clicked_fiend_list)
    button_one.place(x=340, y=550)

    img1 = customtkinter.CTkImage(dark_image=Image.open("data-analysis.png"), size=(150, 150))
    label_seven = CTkLabel(frame1, text="", image=img1)
    label_seven.place(x=20, y=400)


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

textbox_1 = CTkTextbox(frame_3, width=600, height=450, corner_radius=10, fg_color="#1D1E1E")
textbox_1.place(x=35, y=27.5)

steam_logo_img = customtkinter.CTkImage(dark_image=Image.open("SteamLogo.png"), size=(64, 64))
steam_logo_label = CTkLabel(frame_2, text="", image=steam_logo_img)
steam_logo_label.place(x=20, y=15)

steam_text = CTkLabel(frame_2, text="Steam  ", font=("italic", 30, "bold", "underline"))
steam_text.place(x=110, y=35)

# Buttons
button_4 = CTkButton(frame_1, text="Your friends play", width=165, height=150, corner_radius=20,
                     fg_color=button_c, hover_color=button_hc, font=("italic", 15, "bold"))
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

button_6 = CTkButton(frame_2, text="search")
button_6.place(x=700, y=20)

button_7 = CTkButton(frame_2, text="Review")
button_7.place(x=700, y=2)

window.mainloop()
