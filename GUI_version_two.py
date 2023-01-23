from customtkinter import *
import customtkinter
from tkinter import *
from PIL import Image

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
                     text_color="#7c9ab5")
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
