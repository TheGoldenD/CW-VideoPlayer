from tkinter import *
from tkinter import messagebox
from customtkinter import *
import video_library as lib
import font_manager as fonts
#==================MISC Functions==================#
def set_text(text_area, content):
    text_area.delete("1.0", END)
    text_area.insert(1.0, content) 
#================Error Message================#
def errorID():
    messagebox.showwarning(title="Invlid ID", message="Please enter a valid ID")
def errorReview():
    messagebox.showwarning(title="Invalid Rating",message="Please enter a valid number")
def succes():
    messagebox.showinfo(title="New rating saved",message="New rating saved successfully")

class UpdateVideo():
    def __init__(self,window):
        #======================Create Window======================#
        window.geometry("950x350")
        window.title("Create Your Playlist")
        #=========Available Rating=========#
        self.ratingdtb=['1','2','3','4','5']
        
        #=========================Buttons=========================#
        listall_button= CTkButton(window, text="List All Videos",corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command = self.listall)
        listall_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.check_video = CTkButton(window,text="Check Video",corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command = self.displayinfo)
        self.check_video.grid(row=0, column=3, padx=10, pady=10)
        
        self.save = CTkButton(window,text="Save",corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command=self.NewRating)
        self.save.grid(row=0,column=6)
        
        changebutton = CTkButton(window, text="Change Light/Dark mode",corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command=self.changemode)
        changebutton.grid(row=4, column=0, padx=10, pady=10)

        #===========================Text Area===========================#
        self.video_box = CTkTextbox(window, width=300, height=120)
        self.video_box.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        
        self.Videoinfo_box = CTkTextbox(window, width=150, height=120, wrap="none")
        self.Videoinfo_box.grid(row=1, column=3, columnspan=3, sticky="W", padx=10, pady=10)
        
        #======================InFo Label======================#
        self.Video_ID = CTkLabel(window,font=("Arial", 15),text="Enter Video ID")
        self.Video_ID.grid(row=0, column=1, padx=10, pady=10)
        
        self.label = CTkLabel(window,font=("Arial", 15),text="Enter New Rating")
        self.label.grid(row=0, column=4, padx=10, pady=10)
        
        self.status = CTkLabel(window, text="",font=("Arial", 15))
        self.status.grid(row=8, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        #================User Input#================#
        self.ID_input = CTkEntry(window, width=30)
        self.ID_input.grid(row=0, column=2, padx=8, pady=10)
        
        self.rating_input = CTkEntry(window, width=20)
        self.rating_input.grid(row=0, column=5, padx=8, pady=10)
  
        self.listall()
    
    #====================Button Functions====================#
    #===================Recieve and Display Info===================#
    def DisplayInfo(self,key,name,director=None,rating=None,playcount=None):
            director,playcount,rating = self.GetInfo(key)
            info = f"{name}\n{director}\nrating: {rating}\nplays: {playcount}"
            set_text(self.Videoinfo_box,info)
    def GetInfo(self,key):
            director = lib.get_director(key)
            playcount = lib.get_play_count(key)
            rating = lib.get_rating(key)
            return(director,playcount,rating)
    def GetNameAndKey(self):
            key = self.ID_input.get()
            name = lib.get_name(key)
            return(key,name)
    #===========================Show All available video===========================#
    def listall(self):
        showlist = lib.list_all()
        set_text(self.video_box,showlist)
        self.status.configure(text="Status: Showing All Video")
    #==========================Check Video Info==========================#
    def displayinfo(self):
        key , name =self.GetNameAndKey()
        director,rating,playcount = self.GetInfo(key)
        if name is not None:
            self.DisplayInfo( key,name,director,rating,playcount)
        else:
            errorID()
        self.status.configure(text="Status: Checking Video Info")
    #=================Get new Rating=================
    def NewRating(self):
        key , name = self.GetNameAndKey()
        newrate = self.rating_input.get()
        if key:
            if newrate in self.ratingdtb :
                lib.set_rating(key,newrate)
                a = lib.get_rating(key)
                self.DisplayInfo(key,name,rating=a)
                succes()
                self.status.configure(text="Status: Saved new rating")
            elif newrate not in self.ratingdtb:
                errorReview()
                self.status.configure(text="Status: No new rating was saved")
        
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
        
if __name__== "__main__":
    window = CTk()
    set_appearance_mode("dark")
    fonts.configure()
    UpdateVideo (window)
    window.mainloop()