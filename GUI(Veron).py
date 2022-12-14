from tkinter import *

# _______________________________ window colors _______________________________ #
background_color = "#263159"
button_color = "#62B6B7"
white = "white"

# _______________________________ Window starter code _______________________________ #
window = Tk()
window.title("Steam")
window.geometry("1550x820")
window.config(bg=background_color)
steam_icon = PhotoImage(file="Steam_window_logo.png")
window.iconphoto(False, steam_icon)

steam_logo = PhotoImage(file="SteamLogo.png")
steam_logo_label = Label(image=steam_logo, bg=background_color)
steam_logo_label.place(x=20, y=30)
steam_text = Label(text="Steam  ", bg=background_color, fg=white, font=("italic", 30, "bold", "underline"))
steam_text.place(x=110, y=35)

# _______________________________ All toplevel windows _______________________________#


def top_seller_click():
    top = Toplevel()
    top.title("Top sellers")
    top.geometry("1080x720")
    top.config(bg=background_color)
    steam_logo_top = PhotoImage(file="SteamLogo.png")
    steam_logo_label1 = Label(top, image=steam_logo_top, bg=background_color)
    steam_logo_label1.place(x=20, y=30)

    top_seller_text = Label(top, text="Top sellers", bg=background_color, fg=white, font=("italic", 30, "bold", "underline"))
    top_seller_text.place(x=110, y=35)
    top.mainloop()


def top_new_releases():
    top1 = Toplevel()
    top1.title("New releases")
    top1.geometry("1080x720")
    top1.config(bg=background_color)
    steam_logo_top1 = PhotoImage(file="SteamLogo.png")
    steam_logo_label1 = Label(top1, image=steam_logo_top1, bg=background_color)
    steam_logo_label1.place(x=20, y=30)
    new_releases_text = Label(top1, text="New releases", bg=background_color, fg=white, font=("italic", 30, "bold", "underline"))
    new_releases_text.place(x=110, y=35)
    top1.mainloop()


def top_upcoming():
    top2 = Toplevel()
    top2.title("Upcoming")
    top2.geometry("1080x720")
    top2.config(bg=background_color)
    steam_logo_top2 = PhotoImage(file="SteamLogo.png")
    steam_logo_label2 = Label(top2, image=steam_logo_top2, bg=background_color)
    steam_logo_label2.place(x=20, y=30)
    upcoming_text = Label(top2, text="Upcoming", bg=background_color, fg=white, font=("italic", 30, "bold", "underline"))
    upcoming_text.place(x=110, y=35)
    top2.mainloop()


def top_your_friends_play():
    top3 = Toplevel()
    top3.title("Your friends play")
    top3.geometry("1080x720")
    top3.config(bg=background_color)
    steam_logo_top3 = PhotoImage(file="SteamLogo.png")
    steam_logo_label3 = Label(top3, image=steam_logo_top3, bg=background_color)
    steam_logo_label3.place(x=20, y=30)
    your_friends_play_text = Label(top3, text="Your friends play", bg=background_color, fg=white, font=("italic", 30, "bold", "underline"))
    your_friends_play_text.place(x=110, y=35)
    top3.mainloop()


# _______________________________ Main window widgets _______________________________#
browse_categories = Label(text="Browse categories", fg=white, bg=background_color, font=("italic", 10, "bold"))
browse_categories.place(x=10, y=120)

# Top seller button and image.
top_seller = Button(text="Top sellers", bg=background_color, fg=button_color, font=("italic", 10, "bold"), border=0, command=top_seller_click)
top_seller.place(x=30, y=140)
top_seller_image = PhotoImage(file="badge (1).png")
tsi = Label(image=top_seller_image, bg=background_color)
tsi.place(x=10, y=140)

# New releases button and image.
new_releases = Button(text="New releases", bg=background_color, fg=button_color, font=("italic", 10, "bold"), border=0, command=top_new_releases)
new_releases.place(x=30, y=165)
new_releases_image = PhotoImage(file="new-product.png")
nri = Label(image=new_releases_image, bg=background_color)
nri.place(x=10, y=165)

# Upcoming button and image.
upcoming = Button(text="Upcoming", bg=background_color, fg=button_color, font=("italic", 10, "bold"), border=0, command=top_upcoming)
upcoming.place(x=33, y=192)
upcoming_image = PhotoImage(file="upcoming.png")
uci = Label(image=upcoming_image, bg=background_color)
uci.place(x=10, y=192)

# Your friends play button and image.
your_friends_play = Button(text="Your friends play", bg=background_color, fg=button_color, font=("italic", 10, "bold"), border=0, command= top_your_friends_play)
your_friends_play.place(x=33, y=240)
your_friends_play_image = PhotoImage(file="group.png")
yfp = Label(image=your_friends_play_image, bg=background_color)
yfp.place(x=10, y=240)

# Search bar, search text and the search icon.
search_bar_icon = PhotoImage(file="search-icon.png")
sbi = Label(image=search_bar_icon, bg=background_color)
sbi.place(x=1480, y=20)
search_bar = Entry(bg=button_color, borderwidth=0)
search_bar.place(x=1355, y=20)
search_bar_text = Label(text="search", bg=background_color, fg=white, font=("italic", 10, "bold"))
search_bar_text.place(x=1305, y=20)

# Statistics label and text.
statistics = Label(text="Statistics", bg=background_color, fg=white, font=("italic", 10, "bold"), border=0)
statistics.place(x=10, y=220)

# Featured & recommended text with the COD MW 2 image below it.
featured_recommended = Label(text="Featured & recommended", bg=background_color, fg=white, font=("italic", 10, "bold"))
featured_recommended.place(x=300, y=120)
cod_mw_two_image = PhotoImage(file="Call-of-Duty-Modern-Warfare-2.png")
mw_image = Label(image=cod_mw_two_image, bg=background_color)
mw_image.place(x=300, y=145)

# Information about COD MW 2 on the right of the image.
mw_text = Label(text="Call of Duty: Modern Warfare 2", bg=background_color, fg=white, font=("italic", 15, "bold"))
mw_text.place(x=1002, y=147)
available_text = Label(window, text="Available Now !", bg=background_color, fg=white, font=("italic", 12, "bold"))
available_text.place(x=1002, y=180)

window.mainloop()