import tkinter as tk
from tkinter import *
from tkinter import ttk


root = tk.Tk()

root.title("Tetris 2018")
root.configure(bg="grey")

LeftFrame = tk.Frame(root, width = 400, height = 320, bg="black")
LeftFrame.pack(side = LEFT, fill = X, anchor = W)

gameLabel = tk.Label(LeftFrame, font=('arial', 12, 'bold'),
                   text="Tetris Gameplay Area",
                   bd=5, anchor=W)
gameLabel.pack(side = LEFT)

sep = ttk.Separator(root, orient = "vertical")

scoreFrame = tk.Frame(root, width = 80, height = 320, bg="cyan", relief = "ridge")
scoreFrame.pack(side = RIGHT)

scoreLabel = tk.Label(scoreFrame, font=('arial', 12, 'bold'), text = "Score", bd=5, anchor=E)
scoreLabel.pack()

style = ttk.Style(root)
style.configure("TSeparator", background = "red")

root.mainloop()