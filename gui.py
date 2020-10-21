import tkinter as tk
import nanoleaf 
import weather
import time 
import os
import sys
import datetime
import calendar

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
background_image=tk.PhotoImage(file = os.path.join(sys.path[0], "bckg.png"))
Main = tk.Canvas(frame, width=1024, height=600, bd=0, highlightthickness=0)
Main.create_image(0,0,image=background_image,anchor="nw")
Main.pack(side=tk.TOP)

BlueButton = tk.Button(frame, 
                   width=120,
                   height=120,
                   image=null_image,
                   bg="blue",
                   activebackground='blue',
                   command=lambda: nanoleaf.change_color(200)
                   )
RedButton = tk.Button(frame,
                   width=120,
                   height=120,
                   image=null_image,
                   bg="red",
                   activebackground='red',
                   command=lambda: nanoleaf.change_color(0)
                   )
GreenButton = tk.Button(frame,
                   width=120,
                   height=120,
                   image=null_image,
                   bg="green",
                   activebackground='green',
                   command=lambda: nanoleaf.change_color(120)
                   )
PurpleButton = tk.Button(frame,
                   width=120,
                   height=120,
                   image=null_image,
                   bg="purple",
                   activebackground='purple',
                   command=lambda: nanoleaf.change_color(270)
                   )

OrangeButton = tk.Button(frame,
                   width=120,
                   height=120,
                   image=null_image,
                   bg="orange",
                   activebackground='orange',
                   command=lambda: nanoleaf.change_color(30)
                   )

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


CanvasGreenButtpon = Main.create_window(60,0, window=GreenButton)
CanvasBlueButton = Main.create_window(180,0, window=BlueButton)
CanvasRedButton = Main.create_window(300,0, window=RedButton)
CanvasPurpleButton = Main.create_window(420,0, window=PurpleButton)
CanvasOrangeButton = Main.create_window(540,0, window=OrangeButton)
CanvasOffButton = Main.create_window(660,0, window=OffButton)
CanvasOnButton = Main.create_window(780,0, window=WhiteButton)


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
        timeref = Main.create_text(245,440,font="Helvetica 90",text=time_text,fill="white")
    dateref = Main.create_text(175,510,font="Helvetica 25",text=date_text,fill="white")
    
    frame.after(200, updateTime)

def updateWeather():
    global tempref
    descriptor = str(weather.getTemperature()) + " °C, " + weather.getDescriptor()
    Main.delete(tempref)
    tempref = Main.create_text(850,510,font="Helvetica 35",text=descriptor,fill="white")

    # Update every minute
    frame.after(60000, updateTime)

updateWeather()
updateTime()
root.mainloop()