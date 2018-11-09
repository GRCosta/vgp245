import tkinter as tk

counter = 20

def counter_label(label):
    counter = 20
    def countDown():
        global counter
        counter -= 1
        label.config(text=str(counter))
        label.after(1000, countDown)
    countDown()


root = tk.Tk()
root.title("TIME BOMB!!!!")

img = tk.PhotoImage(file='TimeBomb.gif')

label = tk.Label(root, fg='blue', image = img)
label.pack()

counter_label(label)

root.mainloop()