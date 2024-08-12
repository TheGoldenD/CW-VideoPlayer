from tkinter import *
from customtkinter import *
import font_manager as fonts
from check_videos import CheckVideos
from create_list import CreatePlaylist
from update import UpdateVideo
#====================Other Windows====================#
def check_videos_clicked():
    status_lbl.configure(text="Check Videos button was clicked!")
    CheckVideos(CTkToplevel(window))
def create_list_btn_clicked():
    CreatePlaylist(CTkToplevel(window))
def update_btn_clicked():
    UpdateVideo(CTkToplevel(window))
#==============Change Light/Dark mode==============#
mode = "dark"
def changemode():
    global mode
    if mode == "dark":
        set_appearance_mode("light")
        mode = "light"
    else:
        set_appearance_mode("dark")
        mode = "dark"
#==================Creating the GUI==================#
window = CTk()
window.geometry("680x150")
window.title("Video Player")
set_appearance_mode("dark")
fonts.configure()

header_lbl = CTkLabel(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

check_videos_btn = CTkButton(window, text="Check Videos",corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2 ,command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

create_video_list_btn = CTkButton(window, text="Create Video List",corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2 ,command=create_list_btn_clicked)
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_videos_btn = CTkButton(window, text="Update Videos",corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command=update_btn_clicked)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

changebutton = CTkButton(window, text="Change Light/Dark mode",corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command=changemode)
changebutton.grid(row=1, column=3, padx=10, pady=10)

status_lbl = CTkLabel(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
