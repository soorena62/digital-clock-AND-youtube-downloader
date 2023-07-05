import tkinter as tk
from pytube import YouTube

def download_video(): 
    url= ent_url.get()
    try:
        yt = YouTube(url)
        video = yt.streams.first()  
        video.download()
        status_lbl.config(text="Download Successfuly!")  
    except Exception as e:
        status_lbl.config(text="Error in Download Process!")

window = tk.Tk()
window.title("Youtube Downloader")
window.geometry("430x250")    

lbl_url =tk.Label(window,text="Enter URL:")
lbl_url.place(x=5,y=100)

ent_url = tk.Entry(window,width=60)
ent_url.place(x=67,y=100)

btn_dl = tk.Button(window,width=15,text="Download",command=download_video)
btn_dl.place(x=180,y=125)

status_lbl = tk.Label(window, text="")
status_lbl.pack()

window.mainloop()