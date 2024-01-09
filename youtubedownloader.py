import pytube
from tkinter import *
from time import sleep

def downloadYT():
    url = entry.get()
    print(url)
    if(url != ''):
        yt = pytube.YouTube(url= url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=r'Downloads')
version = 1.0

root = Tk()
root.geometry("500x200")
root.configure(bg="#ffffff")
root.title(f'Downloader {version}v')
title = Label(root,text='Youtube Downloader',font=("나눔고딕",20))
label = Label(root,text='URL',font=("나눔고딕",15))
entry = Entry(root,background="#ffff44",width=40)
button = Button(root,text='Download',background="#ff3232",font=("나눔고딕",15,"bold"),fg="white",command=downloadYT)
title.place(x=130,y=50)
label.place(x=100,y=100)
entry.place(x=160,y=105)
button.place(x=200,y=150)
root.mainloop()

