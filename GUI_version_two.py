from customtkinter import *
import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image
import datetime
import requests

# __________________________ Window settings __________________________ #
window = CTk()
window.title("Steam")
cycle = customtkinter.set_appearance_mode("dark")
window.geometry("900x650")
window.minsize(900, 650)
window.maxsize(900, 650)
steam_icon = PhotoImage(file="Steam_window_logo.png")
window.iconphoto(False, steam_icon)

# __________________________ Functions __________________________ #

mode_switch_count = 1


def destroy():
    for widget in window.winfo_children():
        widget.destroy()


def home_screen():
    destroy()
    button_color = "#173b6c"
    button_hover_color = "#156598"

    frame_1_home = CTkFrame(window, width=200, height=475, corner_radius=20)
    frame_1_home.place(x=10, y=145)

    frame_2_home = CTkFrame(window, width=880, height=100, corner_radius=20)
    frame_2_home.place(x=10, y=10)

    steam_logo_img_home = customtkinter.CTkImage(dark_image=Image.open("SteamLogo.png"), size=(64, 64))
    steam_logo_label_home = CTkLabel(frame_2_home, text="", image=steam_logo_img_home)
    steam_logo_label_home.place(x=20, y=15)

    steam_text_home = CTkLabel(frame_2_home, text="Steam  ", font=("italic", 30, "bold", "underline"))
    steam_text_home.place(x=110, y=35)

    # Buttons
    button_1_home = CTkButton(frame_1_home, text="Top sellers", width=165, height=35, corner_radius=20,
                              fg_color=button_color, hover_color=button_hover_color, font=("italic", 15, "bold"),
                              command=top_lvl_top_sellers, text_color="#7c9ab5")
    button_1_home.place(x=20, y=60)

    button_2_home = CTkButton(frame_1_home, text="New", width=165, height=35, corner_radius=20,
                              fg_color=button_color, hover_color=button_hover_color, font=("italic", 15, "bold"),
                              command=top_lvl_new, text_color="#7c9ab5")
    button_2_home.place(x=20, y=105)

    button_3_home = CTkButton(frame_1_home, text="Upcoming", width=165, height=35, corner_radius=20,
                              fg_color=button_color, hover_color=button_hover_color, font=("italic", 15, "bold"),
                              command=top_lvl_upcoming, text_color="#7c9ab5")
    button_3_home.place(x=20, y=150)

    button_4_home = CTkButton(frame_1_home, text="Your friends play", width=165, height=35, corner_radius=20,
                              fg_color=button_color, hover_color=button_hover_color, font=("italic", 15, "bold"),
                              command=top_lvl_your_friends_play, text_color="#7c9ab5")
    button_4_home.place(x=20, y=230)

    button_5_home = CTkButton(frame_1_home, text="Friends list", width=165, height=35, corner_radius=20,
                              fg_color=button_color, hover_color=button_hover_color, font=("italic", 15, "bold"),
                              text_color="#7c9ab5", command=clicked_fiend_list)
    button_5_home.place(x=20, y=275)
    # Labels
    label_1_home = CTkLabel(frame_1_home, text="Browse categories", font=("italic", 15, "bold"))
    label_1_home.place(x=30, y=25)
    label_2_home = CTkLabel(frame_1_home, text="Statistics", font=("italic", 15, "bold"))
    label_2_home.place(x=30, y=200)
    label_3_home = CTkLabel(frame_2_home, text="Search", font=("italic", 15, "bold"))
    label_3_home.place(x=650, y=10)

    # Entry & switch
    entry_1_home = CTkEntry(frame_2_home, width=150, height=30, corner_radius=10, border_color="")
    entry_1_home.place(x=710, y=10)

    switch_home = CTkSwitch(frame_2_home, text="", command=cycle_change, switch_width=40, switch_height=15,
                            fg_color="white",
                            progress_color="#242424")
    switch_home.place(x=820, y=45)


def clicked_fiend_list():
    destroy()
    steam_api_key = "BBD242CD0468A435B14FB923B302231D"
    steam_id = "76561198351674547"

    slink3 = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key="
    slink4 = "&steamid=" + steam_id + "&include_appinfo=1&format=json"
    slink5 = slink3 + steam_api_key + slink4

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
    for j in range(0, length_friend):
        slink6 = "http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=440&key="
        slink7 = "&steamid=" + friends_list[j] + "&include_appinfo=1&format=json"
        slink8 = slink6 + steam_api_key + slink7
        r = requests.get(slink8)

        # convert to JSON and save to another variable
        steam3 = r.json()
        # print(steam3)
        # print(steam3["response"]["game_count"])
    last_seen_list = []
    online_list = ""
    names = ""
    for j in range(0, length_friend):
        slink1 = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="
        slink2 = "&steamids=" + friends_list[j] + "&include_appinfo=1&format=json"
        slink = slink1 + steam_api_key + slink2

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

    # ____________________________ widgets _____________________________ #

    textbox1 = CTkTextbox(window, width=250, height=500, font=("italic", 20))
    textbox1.place(x=37.5, y=100)

    name_str = ""
    counter1 = 1
    for name in names:
        name_str += f"{counter1}: {name}\n\n"
        counter1 += 1
    textbox1.insert(0.0, name_str)

    textbox2 = CTkTextbox(window, width=250, height=500, font=("italic", 20))
    textbox2.place(x=325, y=100)

    online_str = ""
    counter2 = 1
    for status in online_list:
        online_str += f"{counter2}: {status}\n\n"
        counter2 += 1
    textbox2.insert(0.0, online_str)

    textbox3 = CTkTextbox(window, width=250, height=500, font=("italic", 20))
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

    button1 = CTkButton(window, text="Home", width=70, height=50, command=home_screen, fg_color="#3B3B3B",
                        hover_color="#414141")
    button1.place(x=797, y=20)


def cycle_change():
    global cycle, mode_switch_count, button_c, button_hc
    mode_switch_count += 1
    if mode_switch_count % 2:
        cycle = customtkinter.set_appearance_mode("dark")
        button_1.configure(fg_color="#173b6c", hover_color="#156598")
        button_2.configure(fg_color="#173b6c", hover_color="#156598")
        button_3.configure(fg_color="#173b6c", hover_color="#156598")
        button_4.configure(fg_color="#173b6c", hover_color="#156598")
    else:
        cycle = customtkinter.set_appearance_mode("light")
        button_1.configure(fg_color="#242424", hover_color="#535657")
        button_2.configure(fg_color="#242424", hover_color="#535657")
        button_3.configure(fg_color="#242424", hover_color="#535657")
        button_4.configure(fg_color="#242424", hover_color="#535657")


def top_lvl_top_sellers():
    top_1 = CTkToplevel()
    top_1.title("Top sellers")
    customtkinter.set_appearance_mode("dark")
    top_1.geometry("900x650")
    top_1.minsize(900, 650)
    top_1.maxsize(900, 650)
    steam_icon1 = PhotoImage(file="Steam_window_logo.png")
    top_1.iconphoto(False, steam_icon1)


def top_lvl_new():
    top_2 = CTkToplevel()
    top_2.title("New releases")
    customtkinter.set_appearance_mode("dark")
    top_2.geometry("900x650")
    top_2.minsize(900, 650)
    top_2.maxsize(900, 650)
    steam_icon1 = PhotoImage(file="Steam_window_logo.png")
    top_2.iconphoto(False, steam_icon1)


def top_lvl_upcoming():
    top_3 = CTkToplevel()
    top_3.title("Upcoming Games")
    customtkinter.set_appearance_mode("dark")
    top_3.geometry("900x650")
    top_3.minsize(900, 650)
    top_3.maxsize(900, 650)
    steam_icon1 = PhotoImage(file="Steam_window_logo.png")
    top_3.iconphoto(False, steam_icon1)


def top_lvl_your_friends_play():
    top_4 = CTkToplevel()
    top_4.title("Your friends play...")
    customtkinter.set_appearance_mode("dark")
    top_4.geometry("900x650")
    top_4.minsize(900, 650)
    top_4.maxsize(900, 650)
    steam_icon1 = PhotoImage(file="Steam_window_logo.png")
    top_4.iconphoto(False, steam_icon1)


# __________________________ Widgets __________________________ #
# Button colors
button_c = "#173b6c"
button_hc = "#156598"

frame_1 = CTkFrame(window, width=200, height=475, corner_radius=20)
frame_1.place(x=10, y=145)

frame_2 = CTkFrame(window, width=880, height=100, corner_radius=20)
frame_2.place(x=10, y=10)

steam_logo_img = customtkinter.CTkImage(dark_image=Image.open("SteamLogo.png"), size=(64, 64))
steam_logo_label = CTkLabel(frame_2, text="", image=steam_logo_img)
steam_logo_label.place(x=20, y=15)

steam_text = CTkLabel(frame_2, text="Steam  ", font=("italic", 30, "bold", "underline"))
steam_text.place(x=110, y=35)

# Buttons
button_1 = CTkButton(frame_1, text="Top sellers", width=165, height=35, corner_radius=20,
                     fg_color=button_c, hover_color=button_hc, font=("italic", 15, "bold"),
                     command=top_lvl_top_sellers, text_color="#7c9ab5")
button_1.place(x=20, y=60)

button_2 = CTkButton(frame_1, text="New", width=165, height=35, corner_radius=20,
                     fg_color=button_c, hover_color=button_hc, font=("italic", 15, "bold"),
                     command=top_lvl_new, text_color="#7c9ab5")
button_2.place(x=20, y=105)

button_3 = CTkButton(frame_1, text="Upcoming", width=165, height=35, corner_radius=20,
                     fg_color=button_c, hover_color=button_hc, font=("italic", 15, "bold"),
                     command=top_lvl_upcoming, text_color="#7c9ab5")
button_3.place(x=20, y=150)

button_4 = CTkButton(frame_1, text="Your friends play", width=165, height=35, corner_radius=20,
                     fg_color=button_c, hover_color=button_hc, font=("italic", 15, "bold"),
                     command=top_lvl_your_friends_play, text_color="#7c9ab5")
button_4.place(x=20, y=230)

button_5 = CTkButton(frame_1, text="Friends list", width=165, height=35, corner_radius=20,
                     fg_color=button_c, hover_color=button_hc, font=("italic", 15, "bold"),
                     text_color="#7c9ab5", command=clicked_fiend_list)
button_5.place(x=20, y=275)
# Labels
label_1 = CTkLabel(frame_1, text="Browse categories", font=("italic", 15, "bold"))
label_1.place(x=30, y=25)
label_2 = CTkLabel(frame_1, text="Statistics", font=("italic", 15, "bold"))
label_2.place(x=30, y=200)
label_3 = CTkLabel(frame_2, text="Search", font=("italic", 15, "bold"))
label_3.place(x=650, y=10)

# Entry & switch
entry_1 = CTkEntry(frame_2, width=150, height=30, corner_radius=10, border_color="")
entry_1.place(x=710, y=10)

switch = CTkSwitch(frame_2, text="", command=cycle_change, switch_width=40, switch_height=15, fg_color="white",
                   progress_color="#242424")
switch.place(x=820, y=45)

window.mainloop()
