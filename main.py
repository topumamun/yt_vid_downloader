# importing the required libraries

from tkinter import *
from pytube import YouTube

# creating the display window for the app

root = Tk()
root.geometry("500x300")
root.resizable(0, 0)
root.title("Mamun's youtube vid downloader")

# creating the body

Label(root, text="Youtube Video Downloader", font="arial 20 bold").pack()

# creating field to enter link

link = StringVar()
Label(root, text="Paste link here", font="arial 15 bold").place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)

# creating the function to start downloading


def Downloader():
    url = YouTube(str(link.get()))
    # video = url.streams.first()
    # use the above line to get min resolution
    # to get the highest resolution use this line
    video = url.streams.get_highest_resolution()
    # todo: Saving the downloaded vidoe to the windows download folder
    video.download()
    Label(root, text="Downloaded", font="arial 15",).place(x=180, y=210)

# creating the button


Button(root, text="Download", font="arial 15 bold", bg="pale violet red",
       padx=2, command=Downloader).place(x=180, y=150)

root.mainloop()
