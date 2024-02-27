from pytube import YouTube
from pytube.exceptions import RegexMatchError

import tkinter as tk
from tkinter import messagebox
from tkinter import *
import customtkinter

import vlc

# --- Settings
Width = 1920
Height = 1080
root = customtkinter.CTk()
frame = customtkinter.CTkFrame(master=root)
url = customtkinter.CTkEntry(master=frame, width=600, font=('Helvetica', 12))
video_frame = customtkinter.CTkFrame(frame, width=900, height=640)
video_frame.grid(row=0, columnspan=2, pady=12, padx=Width/5.4)

class YoutubeVideo:
    def __init__(self, givenURL):
        self.givenURL = givenURL
    def download_audio(self):
        try:
            yt = YouTube(self.givenURL)
            video = yt.streams.filter(only_audio='True').asc().first()
            video.download("D:\Sterling\Coding\YoutubeDownloader\Audio", filename_prefix="AudioOnly")
        except RegexMatchError as urlWrong:
            print('url entered incorrectly')
            tk.messagebox.showerror('Error', 'URL entered incorrectly')

    def download_video(self):
        try:
            yt = YouTube(self.givenURL)
            video = yt.streams.filter(progressive='True').desc().first()
            video.download("D:\Sterling\Coding\YoutubeDownloader\Video", filename_prefix="Video")
        except RegexMatchError as urlWrong:
            print('url entered incorrectly')
            tk.messagebox.showerror('Error', 'URL entered incorrectly')

# --- Play Video
def download_and_play(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        video_file = stream.download("D:\Sterling\Coding\YoutubeDownloader\Video")
        
        # Create VLC instance
        instance = vlc.Instance()
        player = instance.media_player_new()
        
        # Create media object
        media = instance.media_new(video_file)
        
        # Set media to player
        player.set_media(media)

        # Embed VLC video player in tkinter window
        player_window_id = video_frame.winfo_id()
        player.set_hwnd(player_window_id)

        # Play the video
        player.play()
        
        # Update media controls
        update_media_controls(player)

    except Exception as e:
        print("Error:", e)

# Function to update media controls (play, pause, volume, and time bar)
def update_media_controls(player):
    def update_play_pause_button_text():
        if player.is_playing():
            play_pause_button.config(text="Pause")
        else:
            play_pause_button.config(text="Play")
    def play_pause():
        if player.is_playing():
            player.pause()
        else:
            player.play()
        update_play_pause_button_text()

    def set_volume(volume):
        player.audio_set_volume(int(volume))

    def seek(position):
        length = player.get_length()
        if length > 0:
            target_time = int(int(position) / 100 * length)
            player.set_time(target_time)

    # Volume control
    volume_scale = customtkinter.CTkSlider(master=frame, width=15, height=150, from_=0, to=100, orientation="vertical")
    volume_scale.grid(row=0, column=1, pady=10, padx=380, sticky="SE")

    # Time bar
    time_bar = customtkinter.CTkSlider(master=frame, width=600, height=25, from_=0, to=100, command=seek)
    time_bar.grid(row=1, columnspan=2, pady=5, padx=5)

    # Play/Pause button
    play_pause_button = customtkinter.CTkButton(master=frame, text="Pause", command=play_pause)
    play_pause_button.grid(row=1, column=0, pady=5, padx=5)

    # Update media controls continuously
    def update():
        length = player.get_length()
        if length > 0:
            position = player.get_time() / length * 100
            time_bar.set(position)
        volume_scale.set(player.audio_get_volume())
        root.after(100, update)
    update()

# --- Youtube Downloader Functions
def want_audio(url):
    audio = YoutubeVideo(url)
    audio.download_audio()

def want_video(url):
    video = YoutubeVideo(url)
    video.download_video()

# --- Tkinter GUI (Old)
#request = tk.Tk()
#root.configure(bg='#121212')

class AppWindow():
    # --- Custom TKinter Settings
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    root.geometry(f"{Width}x{Height}")
    root.title('Youtube Downloader')
    root.iconbitmap('YoutubeDownloader\Assets\youtubeicon.ico')

    # --- Create Frame inside window
    frame.pack(pady=12, padx=20, fill='both', expand=True)

    # --- Instruction Text
    instructions = customtkinter.CTkLabel(master=frame, text ='Youtube video URL')
    instructions.grid(row=3, columnspan=2, pady=20)

    # --- Settings for Entry
    url.grid(row=4, columnspan=2, pady=12, padx=Width/5.4)

    # --- MP3/MP4 Download Settings
    Mp3 = customtkinter.CTkButton(master=frame, text="Download Mp3", command=lambda: want_audio(url.get()))
    Mp4 = customtkinter.CTkButton(master=frame, text="Download Mp4", command=lambda: want_video(url.get()))
    Mp3.grid(row=5, column=0, pady=12, padx=Width/5.4)
    Mp4.grid(row=5, column=1, pady=12, padx=Width/5.4)

    # --- Media player
    Play = customtkinter.CTkButton(master=frame, text="Play Video", command=lambda: download_and_play(url.get()))
    Play.grid(row=6, columnspan=2, pady=12, padx=Width/5.4)

    # --- Configure Grid
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)


if __name__ == "__main__":
    AppWindow()
    root.mainloop()
