from tkinter import *
from tkinter import messagebox
from customtkinter import * 
from PIL import *
from CTkListbox import *
import video_library as lib
import font_manager as fonts
import pywhatkit
#==================MISC Functions==================#
def set_text(text_area, content):
    text_area.delete("1.0", END)
    text_area.insert("1.0", content)
    
def add_text(text_area, content):
    text_area.insert("1.0", content + "\n")  
#================Error Message================#
def errorID():
    messagebox.showwarning(title="Invlid ID", message="Please enter a valid ID")
def errorDUP():
    messagebox.showinfo(title="Duplicate found", message="The video has already been added")
def errorNull():
    messagebox.showinfo(title="Playlist Empty",message="Please add a video")
def clearpl():
    messagebox.showinfo(title="Playlist cleared",message="Your playlist has been cleared")
class CreatePlaylist():
    #======================Create Window======================#
        def __init__(self,window):
            window.geometry("950x280")
            window.title("Create Your Playlist")
            #========Video ID List========#
            self.videoplaylist=[]
            self.dfplaylist = 0
            self.showlist = lib.list_all()
            #===================================GUI===================================#

            #===============Display Area===============#
            self.video_box = CTkTextbox(window, width=400, height=100)
            self.video_box.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
            
            self.Videoinfo_box = CTkTextbox(window, width=150, height=120)
            self.Videoinfo_box.grid(row=1, column=3, columnspan=3, sticky="W", padx=10, pady=10)
            
            self.playlist = CTkTextbox(window, width=300, height=120, wrap="none")
            self.playlist.grid(row=1, column=5, columnspan=3, sticky="W", padx=10, pady=10)
            
            #=============Info Text=============#
            self.Video_ID = CTkLabel(window,text="Enter Video ID",font=("Arial", 15),fg_color="transparent")
            self.Video_ID.grid(row=0, column=1, padx=10, pady=10)
            
            self.status = CTkLabel(window, text="", font=("Arial", 15))
            self.status.grid(row=8, column=0, columnspan=4, sticky="W", padx=10, pady=10)
            
            #=========================Buttons=========================#
            listall_button= CTkButton(window, text="List All Videos", corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command = self.listall)
            listall_button.grid(row=0, column=0, padx=10, pady=10)
            
            self.check_video = CTkButton(window,text="Check Video", corner_radius=32 ,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command = self.displayinfo)
            self.check_video.grid(row=0, column=3, padx=10, pady=10)
            
            self.add_video = CTkButton(window,text="Add Video",corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command=self.add_btn_clicked)
            self.add_video.grid(row=0, column=5, padx=8, pady=10)
            
            self.delete_list = CTkButton(window,text="Clear list",corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command=self.clear_btn_clicked)
            self.delete_list.grid(row=0, column=6, padx=8, pady=10)
            
            self.playvideo = CTkButton(window,text="Play Video",corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command=self.PlayVid)
            self.playvideo.grid(row=3, column=5, padx=8, pady=10)
            
            self.next = CTkButton(window,text=">>>",corner_radius=32,width=30,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command=self.Next)
            self.next.grid(row=3, column=6, padx=8, pady=10)
            
            self.prev = CTkButton(window,text="<<<",corner_radius=32,width=30,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command=self.Prev)
            self.prev.grid(row=3, column=6, padx=8,sticky= "W", pady=10)
            
            self.changebutton = CTkButton(window, text="Change Light/Dark mode",corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",border_color="#FFCC70",border_width=2,command=self.changemode)
            self.changebutton.grid(row=3, column=0, padx=10, pady=10)
            
            #======User Input======#
            self.ID_input = CTkEntry(window, width=35,placeholder_text="'01'")
            self.ID_input.grid(row=0, column=2, padx=8, pady=10)
            
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
        def GetUrl(self,key):
            url = lib.get_url(key)
            return url
            
        #==========Add a video to the playlist==========#
        def add_btn_clicked(self):
            key , name = self.GetNameAndKey()
            if name is not None:
                if key not in self.videoplaylist:
                    self.videoplaylist.append(key)
                    addname=f"{name}"
                    add_text(self.playlist,addname)
                    print(self.videoplaylist)
                else:
                    errorDUP()
            else:
                errorID()
            self.status.configure(text="Status: Added a video")       
            
        #===============Clear PLaylist===============#
        def clear_btn_clicked(self):
            self.playlist.delete("1.0", "end")
            self.videoplaylist.clear()
            clearpl()
            
        #========Show All available video========#
        def listall(self):
            showlist = lib.list_all()
            set_text(self.video_box,showlist)
            self.status.configure(text="Status: Showing All Video")
            
        #==========Check Video Info==========#   
        def displayinfo(self):
            key , name =self.GetNameAndKey()
            director,rating,playcount = self.GetInfo(key)
            if name is not None:
                self.DisplayInfo( key,name,director,rating,playcount)
            else:
                errorID()
            self.status.configure(text="Status: Checking Video Info")
            
        #===============Play Video===============#
        def PlayVid(self):
                if len(self.videoplaylist) == 0:
                    errorNull()
                else:   
                        key = self.videoplaylist[self.dfplaylist]
                        url = self.GetUrl(key)
                        lib.increment_play_count(key)
                        name = lib.get_name(key)
                        pywhatkit.playonyt(url)
                        self.DisplayInfo(key,name)
                self.status.configure(text="Status: Playing Video")
                
        #===========Choose a song===========#    
        def Next(self):
            if self.dfplaylist < len(self.videoplaylist)-1:
                self.dfplaylist += 1
            elif self.dfplaylist > len(self.videoplaylist)-1:
                self.dfplaylist = len(self.videoplaylist)-1
            key = self.videoplaylist[self.dfplaylist]
            name = lib.get_name(key)
            self.DisplayInfo(key,name)
            self.status.configure(text="Status: Playing the next video")
        def Prev(self):
            if self.dfplaylist != 0:
                self.dfplaylist -= 1
            elif self.dfplaylist < 0:
                self.dfplaylist =0
            key = self.videoplaylist[self.dfplaylist]
            name = lib.get_name(key)
            self.DisplayInfo(key,name)
            self.status.configure(text="Status: Playing the next video")
            
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
            
if __name__ == "__main__":         
    window = CTk()
    set_appearance_mode("dark")
    fonts.configure()
    CreatePlaylist (window)
    window.mainloop()