import tkinter as tk
import connection
    

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

BlueButton = tk.Button(frame, 
                   width=30,
                   height=30,
                   bg="blue",
                   activebackground='blue',
                   command=lambda: connection.change_color(200)
                   )
BlueButton.pack(side=tk.LEFT)
RedButton = tk.Button(frame,
                   width=30,
                   height=30,
                   bg="red",
                   activebackground='red',
                   command=lambda: connection.change_color(0)
                   )
RedButton.pack(side=tk.LEFT)
GreenButton = tk.Button(frame,
                   width=30,
                   height=30,
                   bg="green",
                   activebackground='green',
                   command=lambda: connection.change_color(120)
                   )
GreenButton.pack(side=tk.LEFT)

root.mainloop()