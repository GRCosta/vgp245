# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 19:28:30 2018

@author: grcos
"""

import tkinter as tk

def winning():
    print("You Win!")

def increment():
    global count
    if count.get() < 10: 
        count.set(count.get() + 1)
    else:
        winning()

root = tk.Tk()

count=tk.IntVar()
frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, textvariable=count)
label.pack()

button = tk.Button(frame, text="Quit", fg="red", command=quit)
button.pack(side=tk.LEFT)

button2 = tk.Button(frame, text="Press me", fg="blue", command=increment)
button2.pack()

root.mainloop()