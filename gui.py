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
bckg = Main.create_image(0,0,image=background_image,anchor="nw")
Main.pack(side=tk.TOP)

b1 = tk.Button(frame,
                   width=103,
                   height=120,
                   image=null_image,
                   bg="#FF9900",
                   activebackground='#FF9900',
                   command=lambda: colorWrapper(36, 1)
                   )

b2 = tk.Button(frame,
                   width=103,
                   height=120,
                   image=null_image,
                   bg="#CCFF00",
                   activebackground='#CCFF00',
                   command=lambda: colorWrapper(72, 2)
                   )

b3 = tk.Button(frame,
                   width=103,
                   height=120,
                   image=null_image,
                   bg="#33FF00",
                   activebackground='#33FF00',
                   command=lambda: colorWrapper(108, 3)
                   )

b4 = tk.Button(frame,
                   width=103,
                   height=120,
                   image=null_image,
                   bg="#00FF66",
                   activebackground='#00FF66',
                   command=lambda: colorWrapper(144, 4)
                   )

b5 = tk.Button(frame,
                   width=103,
                   height=120,
                   image=null_image,
                   bg="#00FFFF",
                   activebackground='#00FFFF',
                   command=lambda: colorWrapper(180, 5)
                   )

b6 = tk.Button(frame,
                   width=103,
                   height=120,
                   image=null_image,
                   bg="#0066FF",
                   activebackground='#0066FF',
                   command=lambda: colorWrapper(216, 6)
                   )

b7 = tk.Button(frame,
                   width=103,
                   height=120,
                   image=null_image,
                   bg="#3300FF",
                   activebackground='#3300FF',
                   command=lambda: colorWrapper(252, 7)
                   )

b8 = tk.Button(frame,
                   width=103,
                   height=120,
                   image=null_image,
                   bg="#CC00FF",
                   activebackground='#CC00FF',
                   command=lambda: colorWrapper(288, 8)
                   )

b9 = tk.Button(frame,
                   width=103,
                   height=120,
                   image=null_image,
                   bg="#FF0099",
                   activebackground='#FF0099',
                   command=lambda: colorWrapper(324, 9)
                   )

b10 = tk.Button(frame,
                   width=103,
                   height=120,
                   image=null_image,
                   bg="#FF0004",
                   activebackground='#FF0004',
                   command=lambda: colorWrapper(360, 10)
                   )


OffButton = tk.Button(frame,
                   width=103,
                   height=120,
                   image=null_image,
                   bg="black",
                   activebackground='black',
                   command=lambda: nanoleaf.off()
                   )

WhiteButton = tk.Button(frame,
                   width=103,
                   height=120,
                   image=null_image,
                   bg="white",
                   activebackground='white',
                   fg="white",
                   command=lambda: nanoleaf.white()
                   )
C1 = Main.create_window(51,10, window=b1)
C2 = Main.create_window(154,10, window=b2)
C3 = Main.create_window(256,10, window=b3)
C4 = Main.create_window(358,10, window=b4)
C5 = Main.create_window(461,10, window=b5)
C6 = Main.create_window(563,10, window=b6)
C7 = Main.create_window(666,10, window=b7)
C8 = Main.create_window(768,10, window=b8)
C9 = Main.create_window(870,10, window=b9)
C10 = Main.create_window(973,10, window=b10)


CanvasOffButton = Main.create_window(780,600, window=OffButton)
CanvasOnButton = Main.create_window(887,600, window=WhiteButton)


#slider = tk.Scale(frame, from_=0, to=360, orient="horizontal", length=850, label="")
#CanvasScale = Main.create_window(512,4, window=slider)

'''
def updateSlider():
    global color
    new_color = slider.get()
    if new_color != color:
        nanoleaf.change_color(slider.get())
        color = new_color
    frame.after(100, updateSlider)
'''

# Arg 1: what is sent to the nanoleaf, 2: the background changes with the color.
def colorWrapper(color, picnum):
    global C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,bckg
    nanoleaf.change_color(color)
    Main.delete(bckg)
    background_image=tk.PhotoImage(file = os.path.join(sys.path[0], "bckg" + str(picnum) + ".png"))
    print(os.path.join(sys.path[0], "bckg" + str(picnum) + ".png"))
    Main.create_image(0,0,image=background_image,anchor="nw")
    Main.image=background_image
    '''
    C1 = Main.create_window(51,10, window=b1)
    C2 = Main.create_window(154,10, window=b2)
    C3 = Main.create_window(256,10, window=b3)
    C4 = Main.create_window(358,10, window=b4)
    C5 = Main.create_window(461,10, window=b5)
    C6 = Main.create_window(563,10, window=b6)
    C7 = Main.create_window(666,10, window=b7)
    C8 = Main.create_window(768,10, window=b8)
    C9 = Main.create_window(870,10, window=b9)
    C10 = Main.create_window(973,10, window=b10)
    '''
    updateWeather()
    updateTime()




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
    dateref = Main.create_text(190,510,font="Helvetica 25",text=date_text,fill="white")
    
    frame.after(1000, updateTime)

def updateWeather():
    global tempref
    info = weather.getWeather()
    locale = weather.getLocation()
    descriptor = str(info[0]) + " °C, " + info[1] + "\n" + locale
    Main.delete(tempref)
    tempref = Main.create_text(850,480,font="Helvetica 30",text=descriptor,fill="white")

    # Update every minute
    frame.after(60000, updateTime)

#updateSlider()
updateWeather()
updateTime()
root.mainloop()