from tkinter import *
from pytube import YouTube
import os
from plyer import notification

root = Tk()
root.title("Youtube Downloader")
root.geometry('700x200')
root.resizable(width=False,height=False)
label_1 = Label(root,text="Youtube Downloader",justify="center",height=2,font = 'calibri 14 bold')
url_var = StringVar()

def download(ignore):
    root.destroy()
    url = YouTube(str(url_var.get()))
    video = url.streams.filter(file_extension='mp4').get_highest_resolution()#get_by_itag(22) #itag 299 is for 1080p and 60fps
    #print(video)
    video.download(output_path="C:\\Tarakesh\\My Work\\Python\\Completely by me\\Youtube Downloader\\Downloads")
    notification.notify(
        title = 'Youtube Downloader',
        message = 'Download Complete!',
        app_icon = None,
        timeout = 8,
    )
    os.startfile("C:\\Tarakesh\\My Work\\Python\\Completely by me\\Youtube Downloader\\Downloads")

label_2 = Label(root,text="Paste link here:",justify="center",height=0,font = 'calibri 12')
url_entry = Entry(root,width=50,justify='center',textvariable=url_var)
url_entry.bind('<Return>',download)
#button = Button(root,text="Download",command=download)

label_1.pack()
label_2.pack()
url_entry.pack()
#button.pack()
root.mainloop()