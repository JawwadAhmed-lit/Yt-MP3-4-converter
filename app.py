import os

import moviepy.editor
from tkinter.filedialog import *

import yt_dlp
import customtkinter as ctk
import pandas as pd



def download_video_from_file():
    try:
        status_label.pack(pady=10)
        progress_label.pack(pady=10)
        progress.pack(pady=10)
        pdReader = pd.read_csv('links.csv')
        linksList = []
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'progress_hooks': [my_hook]
        }
        for link in pdReader['links']:
            linksList.append(link)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for link in linksList:
                os.path.join("downloads", f"{ydl.extract_info(link, download=True).get('title')}.mp4")
                ydl.download([link])
            status_label.configure(text="Downloaded Successfully",text_color="white",fg_color="green")
    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}",text_color="white",fg_color="red")





def download_video():
    url = entry.get()
    status_label.pack(pady=10)
    progress_label.pack(pady=10)
    progress.pack(pady=10)
    try:
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'progress_hooks': [my_hook]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            os.path.join("downloads",f"{ydl.extract_info(url, download=True).get('title')}.mp4")
            ydl.download(url)
            status_label.configure(text="Downloaded Successfully",text_color="white",fg_color="green")

    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}",text_color="white",fg_color="red")

def my_hook(d):
    if d['status'] == 'downloading':
#         update the progress bar
        progress['value'] = d['_percent_str']
        progress_label.configure(text=f"{d['_percent_str']} downloaded")
        progress_label.update()
    elif d['status'] == 'finished':
        progress_label.configure(text="100% downloaded")
        progress['value'] = "100"
        progress_label.update()
        status_label.configure(text="Downloaded Successfully",text_color="white",fg_color="green")

def convert_mp3():

    video_file = askopenfilename()

    video = moviepy.editor.VideoFileClip(video_file)
    print(video)
    audio = video.audio

    # Extract the video title from the video file path
    video_title = os.path.splitext(os.path.basename(video_file))[0]

    # Create the path to the output file
    output_file = os.path.join('downloads', f"{video_title}.mp3")

    # Write the audio to the output file
    audio.write_audiofile(output_file)
    status_label.configure(text="Converted Successfully",text_color="white",fg_color="green")
    status_label.pack(pady=10)
    video.close()


# Create the root window
root = ctk.CTk()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

# we Title of the window
root.title("Yout To Mp4/Mp3 Downloader")

# Set the size of the window
root.geometry("750x500")
root.maxsize(1080,720)
root.minsize(750,500)

# creating a frame
frame = ctk.CTkFrame(root)
frame.pack(fill=ctk.BOTH, expand=True,padx=10,pady=10)

# creating a label and text entry for the link
label = ctk.CTkLabel(frame, text="Enter the link: ")
entry = ctk.CTkEntry(frame, width=500, height=40)
label.pack(pady=10)
entry.pack(pady=10)

# create a download button
downloadButt = ctk.CTkButton(frame, text="Download",command=download_video)
downloadButt.pack(pady=10)

# create a download from file button
downloadFileButt = ctk.CTkButton(frame, text="Download from csv file",command=download_video_from_file)
downloadFileButt.pack(pady=10)

# create a progress bar
progress_label = ctk.CTkLabel(frame, text="0%")


progress = ctk.CTkProgressBar(frame, width=400)


# create a status label
status_label = ctk.CTkLabel(frame, text="Status")

# create a convert button
convertButt = ctk.CTkButton(frame, text="Select MP3 to Convert",command=convert_mp3)
convertButt.pack(pady=10)



# run
root.mainloop()