from tkinter import *
from tkinter import messagebox
from customtkinter import *
import video_library as lib
import font_manager as fonts

#==================MISC Functions==================#
#Function to clear and show the available video info
def set_text(text_area, content):
    text_area.delete("1.0", END) #delete the existing content
    text_area.insert(1.0, content)  #add the original content
def errorID():
    messagebox.showwarning(title="Invlid ID", message="Please enter a valid ID")
#Create the GUI
class CheckVideos():
    #======================Create Window======================#
    def __init__(self, window):
        window.geometry("750x350")
        window.title("Check Videos")

        #=========================Buttons=========================#
        list_videos_btn = CTkButton(window, text="List All Videos", corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2 ,command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        check_video_btn = CTkButton(window, text="Check Video", corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2 ,command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)
        
        changebutton = CTkButton(window, text="Change Light/Dark mode",corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command=self.changemode)
        changebutton.grid(row=3, column=0, padx=10, pady=10)
        #=============Info Text=============#
        enter_lbl = CTkLabel(window,font=("Arial", 15) ,text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.status_lbl = CTkLabel(window,text="", font=("Aria", 15))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        
        #======User Input======#
        self.input_txt = CTkEntry(window, width=30)
        self.input_txt.grid(row=0, column=2,sticky ="W" ,padx=10, pady=10)
        
        #===============Display Area===============#
        self.list_txt = CTkTextbox(window, width=400, height=120)
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        
        self.video_txt = CTkTextbox(window, width=150, height=120)
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)
        self.list_videos_clicked()
        
    #====================Button Functions====================#
    #==========Check Video Info==========#   
    def check_video_clicked(self):
        key = self.input_txt.get() #Get key from user input
        name = lib.get_name(key)   #Get name from the key from the said input
        if name is not None:
            director = lib.get_director(key) #Get info from the library
            rating = lib.get_rating(key)    #Get info from the library
            play_count = lib.get_play_count(key)    #Get info from the library
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            errorID()
        self.status_lbl.configure(text="Check Video button was clicked!")
    #========Show All available video========#
    def list_videos_clicked(self):
        video_list = lib.list_all() #List all video and info
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")
    #================Change Light and Dark mode===================#
    mode = "dark"
    def changemode(self):
        global mode
        if self.mode == "dark":
            set_appearance_mode("light")
            self.mode = "light"
        else:
            set_appearance_mode("dark")
            self.mode = "dark"      
            
if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = CTk()        # create a TK object
    set_appearance_mode("dark")
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc