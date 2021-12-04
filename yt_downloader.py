from tkinter import *
from tkinter import messagebox

from pytube import YouTube

root = Tk()
root.geometry("600x600")
bgm_img = PhotoImage(file="pic2.png")
img31 = Label(root, image=bgm_img)
img31.place(x=0, y=0)
# root.resizable(False, False)
PATH = "C:\\Users\\parte\\Desktop\\YT_DOWNLOADER"
# yt = PhotoImage(file='bcd.png')
root.iconbitmap(False, 'yotube_icon.ico')
root.title("YOUTUBE VIDEO DOWNLOADER")

Label(root, text="YOUTUBE VIDEO DOWNLOADER", font=("Arial", 25, 'bold')).pack(padx=20, pady=20)
Label(root, text="Enter Your Link Below", font=("Arial", 20, 'bold')).pack(padx=25, pady=25)

Entry_box = StringVar()

Entry(root, textvariable=Entry_box, font=('Arial', 15, 'bold'), bg='white', fg='red', width=40).pack(padx=20, pady=20)


def download_video():
    url = Entry_box.get()
    video_title = YouTube(url).title
    video_img = YouTube(url).thumbnail_url
    print(video_img)
    Label(root, text=video_title, font=("Arial", 15, 'bold'), bg="white", fg='red').pack(padx=25, pady=25)
    btn1 = Button(root, text="High Resolution", command=video_download1, font=("Arial", 10, 'bold'), bg='white',
                  width=20,
                  height=3).pack(padx=20, pady=2)

    btn2 = Button(root, text="Low Resolution", command=video_download2, font=("Arial", 10, 'bold'), bg='white',
                  width=20,
                  height=3).pack(padx=20, pady=2)


def video_download1():
    url1 = Entry_box.get()
    my_video = YouTube(url1)

    my_video = my_video.streams.get_highest_resolution()
    my_video.download(PATH)
    messagebox.showinfo('DOWNLOADED', 'YOUR VIDEO DOWNLOADED SUCCESSFULLY')


def video_download2():
    url1 = Entry_box.get()
    my_video = YouTube(url1)
    my_video = my_video.streams.get_lowest_resolution()
    my_video.download(PATH)
    messagebox.showinfo('DOWNLOADED', 'YOUR VIDEO DOWNLOADED SUCCESSFULLY')


btn = Button(root, text="SUBMIT", command=download_video, font=("Arial", 10, 'bold'), bg='white', width=10,
             height=1).pack(padx=20, pady=2)

root.mainloop()
