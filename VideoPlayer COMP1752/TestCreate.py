from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class CreateVideoList:
    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.window.geometry("600x500")  
        self.window.title("Create Video Playlist")

        # Simulated video database with video numbers and names
        self.video_db = {
            "1": "Video 1: caulk",
            "2": "Video 2: balls",
            "3": "Video 3: ur mom",
            "4": "Video 4: funny?where",
            "5": "Video 5: no idea"
        }

        
        self.playlist = []
        self.play_counts = {video: 0 for video in self.video_db.values()}

        # Video number entry
        self.video_num_label = ttk.Label(self.window, text="Enter Video Number:")
        self.video_num_label.pack(pady=10)
        self.video_num_entry = ttk.Entry(self.window)
        self.video_num_entry.pack(pady=5)

    
        self.add_button = ttk.Button(self.window, text="Add to Playlist", command=self.add_to_playlist, bootstyle="success")
        self.add_button.pack(pady=10)

        
        self.playlist_area = ttk.Text(self.window, height=10, width=50,  state="disabled")
        self.playlist_area.pack(pady=10)
        self.play_button = ttk.Button(self.window, text="Play Playlist", command=self.play_playlist, bootstyle="info")
        self.play_button.pack(pady=5)

        
        self.play_count_area = ttk.Text(self.window, height=6, width=50,  state="disabled")
        self.play_count_area.pack(pady=10)
        self.reset_button = ttk.Button(self.window, text="clear", command=self.reset_playlist, bootstyle="danger")
        self.reset_button.pack(pady=5)

        self.message_label = ttk.Label(self.window, text="")
        self.message_label.pack(pady=10)

    def add_to_playlist(self):
        video_num = self.video_num_entry.get().strip()

        if video_num in self.video_db:
            video_name = self.video_db[video_num]
            self.playlist.append(video_name)
            self.update_playlist_display()
            self.message_label.configure(text="Video added to playlist.", bootstyle="success")
        else:
            self.message_label.configure(text="Invalid video number,try again bozo", bootstyle="danger")

    def update_playlist_display(self):
        self.playlist_area.configure(state="normal")
        self.playlist_area.delete(1.0, END)
        for video in self.playlist:
            self.playlist_area.insert(END, f"{video}\n")
        self.playlist_area.configure(state="disabled")

    def play_playlist(self):
        if self.playlist:
            for video in self.playlist:
                self.play_counts[video] += 1
            self.message_label.configure(text="Playing playlist...", bootstyle="info")
            self.update_play_count_display()
        else:
            self.message_label.configure(text="Playlist is empty.", bootstyle="warning")

    def update_play_count_display(self):
        self.play_count_area.configure(state="normal")
        self.play_count_area.delete(1.0, END)
        for video, count in self.play_counts.items():
            if count > 0:
                self.play_count_area.insert(END, f"{video} - Play Count: {count}\n")
        self.play_count_area.configure(state="disabled")

    def reset_playlist(self):
        self.playlist = []
        self.update_playlist_display()
        self.play_count_area.configure(state="normal")
        self.play_count_area.delete(1.0, END)
        self.play_count_area.configure(state="disabled")
        self.message_label.configure(text="Playlist has been reset.", bootstyle="info")
        
if __name__ == "__main__":
    window = Tk()
    CreateVideoList (window)
    window.mainloop()