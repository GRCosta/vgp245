# python3
import tkinter as tk
from tkinter.ttk import Separator, Style


fen = tk.Tk()

left = tk.Frame(fen, bg="black",width=320, height=480)

# to prevent the frame from adapting to its content :
left.pack_propagate(False)
tk.Label(left, text="Left frame", fg="white", bg="black", anchor="center", justify="center").pack()
left.grid(column=0, row = 0, pady=5 ,padx=10, sticky="n")
sep = Separator(fen, orient="vertical")
sep.grid(column=1, row=0, sticky="ns")

# edit: To change the color of the separator, you need to use a style
sty = Style(fen)
sty.configure("TSeparator", background="red")

right= tk.Frame(fen, bg="black",width=100, height=100)
right.pack_propagate(False)
tk.Label(right, text="Right frame", fg="white", bg="black").pack()
right.grid(column=2, row = 0, pady=5,padx=10, sticky="n")

fen.mainloop()