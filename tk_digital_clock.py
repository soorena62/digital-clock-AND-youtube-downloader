from tkinter import *
import time

window = Tk()
window.title("Digital Clock")
window.geometry("350x170")

def show_time():
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    am_pm = time.strftime('%p')
    day = time.strftime('%A')
    zone = time.strftime('%Z')
    
    mytext = hour + ":" + minute + ":" + second + " " + am_pm
    calend_text = day + ", " + zone
    lbl_time.config(text = mytext)   #show mytext instead lbl_time(text)
    lbl_calendar.config(text = calend_text)
    lbl_time.after(1000, show_time)  #update second 
    
lbl_time = Label(window,
text="Hello Word", 
font=('Digital-5', 30, 'bold'), 
fg='darkred', 
bg= 'green')

lbl_calendar = Label(window, 
text = "day",
font=('Arial', 18),
fg='White',
bg='Black')

show_time()
lbl_time.pack()
lbl_calendar.pack()
window.mainloop()
