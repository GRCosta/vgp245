# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:36:01 2018

@author: grcosta
"""

import tkinter
import tkinter.scrolledtext as scroll
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
from tkinter import END
import datetime


root = tkinter.Tk(className="#Virtual Post-it")
notePad = scroll.ScrolledText(root, width=80, height=50, background="light yellow")
frame = tkinter.Frame(root)
frame.pack(side=tkinter.TOP)

# Function definitions
def comm_open_file():
    file = filedialog.askopenfile(parent = root, mode = 'rb', title = 'Select a file')
    if file != None:
        contents = file.read()
        notePad.insert('1.0', contents)
        file.close()
        
def comm_save_file():
    file = filedialog.asksaveasfile(mode='w')
    if file != None:
        data = notePad.get('1.0', END + '-1c')
        file.write(data)
        file.close()

def comm_quit():
    if tkinter.messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def comm_about():
    label = messagebox.showinfo("About", "Virtual Post-it \n Copyright @grcosta")

def comm_time_stamp():
    timestamp = datetime.datetime.now().strftime('%d %B %Y %H:%M:%S - \n')
    notePad.insert(tkinter.INSERT, "\n")
    notePad.insert(tkinter.INSERT, timestamp)

# For the menus
menu = tkinter.Menu(root)
root.config(menu = menu)

# 1. File menu
fileMenu = tkinter.Menu(menu)
menu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "New")
fileMenu.add_command(label = "Open...", command = comm_open_file)
fileMenu.add_command(label = "Save", command = comm_save_file)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = comm_quit)

helpMenu = tkinter.Menu(menu)
menu.add_cascade(label = "Help", menu = helpMenu)
helpMenu.add_command(label = "About...", command = comm_about)

bTimeStamp = tkinter.Button(frame, text = 'TimeStamp', fg = 'blue', width = 20, command = comm_time_stamp)
bTimeStamp.pack(side=tkinter.RIGHT)
notePad.pack()
root.mainloop()


