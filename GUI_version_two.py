from customtkinter import *
import customtkinter
from tkinter import *
from PIL import Image


# __________________________ Window settings __________________________ #
top1 = CTk()
top1.title("Steam")
customtkinter.set_appearance_mode("dark")
top1.geometry("900x650")
top1.minsize(900, 650)
top1.maxsize(900, 650)
steam_icon = PhotoImage(file="Steam_window_logo.png")
top1.iconphoto(False, steam_icon)

steam_logo_img = customtkinter.CTkImage(dark_image=Image.open("SteamLogo.png"), size=(64, 64))
steam_logo_label = CTkLabel(top1, text="", image=steam_logo_img)
steam_logo_label.place(x=20, y=30)

steam_text = CTkLabel(top1, text="Steam  ", font=("italic", 30, "bold", "underline"))
steam_text.place(x=110, y=55)


# __________________________ Functions __________________________ #

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
button_c = "#0a1e41"
button_hc = "#156598"

frame_1 = CTkFrame(top1, width=200, height=500, corner_radius=20)
frame_1.place(x=10, y=120)

# Buttons
button_1 = CTkButton(frame_1, text="Top sellers", width=165, height=35, corner_radius=20,
                     fg_color="#173b6c", hover_color=button_hc, font=("italic", 15, "bold"),
                     command=top_lvl_top_sellers)
button_1.place(x=20, y=60)

button_2 = CTkButton(frame_1, text="New", width=165, height=35, corner_radius=20,
                     fg_color="#173b6c", hover_color=button_hc, font=("italic", 15, "bold"),
                     command=top_lvl_new)
button_2.place(x=20, y=105)

button_3 = CTkButton(frame_1, text="Upcoming", width=165, height=35, corner_radius=20,
                     fg_color="#173b6c", hover_color=button_hc, font=("italic", 15, "bold"),
                     command=top_lvl_upcoming)
button_3.place(x=20, y=150)

button_4 = CTkButton(frame_1, text="your friends play", width=165, height=35, corner_radius=20,
                     fg_color="#173b6c", hover_color=button_hc, font=("italic", 15, "bold"),
                     command=top_lvl_your_friends_play)
button_4.place(x=20, y=230)

# Labels
label_1 = CTkLabel(frame_1, text="Browse categories", font=("italic", 15, "bold"))
label_1.place(x=30, y=20)
label_2 = CTkLabel(frame_1, text="Statistics", font=("italic", 15, "bold"))
label_2.place(x=60, y=195)

top1.mainloop()
