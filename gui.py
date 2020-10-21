import tkinter as tk
import nanoleaf 
import weather
import time 
import os
import sys
import datetime
import calendar

# Color state
color = 0

# Tkinter Labels
timeref = None
dateref = None
tempref = None

# Generating root and frame
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# Setting up background images and buttons
null_image = tk.PhotoImage(width=0, height=0)
background_image=tk.PhotoImage(file = os.path.join(sys.path[0], "bckg2.png"))
Main = tk.Canvas(frame, width=1024, height=600, bd=0, highlightthickness=0)
Main.create_image(0,0,image=background_image,anchor="nw")
Main.pack(side=tk.TOP)


OffButton = tk.Button(frame,
                   width=120,
                   height=120,
                   image=null_image,
                   bg="black",
                   activebackground='black',
                   command=lambda: nanoleaf.off()
                   )

WhiteButton = tk.Button(frame,
                   width=120,
                   height=120,
                   image=null_image,
                   bg="white",
                   activebackground='white',
                   fg="white",
                   command=lambda: nanoleaf.white()
                   )

CanvasOffButton = Main.create_window(780,600, window=OffButton)
CanvasOnButton = Main.create_window(900,600, window=WhiteButton)


slider = tk.Scale(frame, from_=0, to=360, orient="horizontal", length=1024, label="")
CanvasScale = Main.create_window(512,2, window=slider)

def updateSlider():
    global color
    new_color = slider.get()
    if new_color != color:
        nanoleaf.change_color(slider.get())
        color = new_color
    frame.after(100, updateSlider)

# Initializes the date/time strings and updates every 200 msec
def updateTime():
    now = datetime.datetime.now()
    month = now.strftime("%B")
    date = now.strftime("%d")
    day = calendar.day_name[datetime.date.today().weekday()]
    global timeref
    global dateref
    time_text = time.strftime("%I:%M%p")
    date_text = day + ", " + month + " " + date
    Main.delete(timeref)
    Main.delete(dateref)
    if time_text[0] == "0":
        time_text = time_text[1:]
        timeref = Main.create_text(215,440,font="Helvetica 90",text=time_text,fill="white")
    else:
        timeref = Main.create_text(250,440,font="Helvetica 90",text=time_text,fill="white")
    dateref = Main.create_text(180,510,font="Helvetica 25",text=date_text,fill="white")
    
    frame.after(200, updateTime)

def updateWeather():
    global tempref
    info = weather.getWeather()
    locale = weather.getLocation()
    descriptor = str(info[0]) + " °C, " + info[1] + "\n" + locale
    Main.delete(tempref)
    tempref = Main.create_text(850,480,font="Helvetica 30",text=descriptor,fill="white")

    # Update every minute
    frame.after(60000, updateTime)

updateSlider()
updateWeather()
updateTime()
root.mainloop()