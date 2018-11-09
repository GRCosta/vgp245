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

#img = tk.PhotoImage(file='TimeBomb.gif', format="gif -index 2")

frames = [tk.PhotoImage(file='TimeBomb.gif',format = 'gif -index %i' %(i)) for i in range(20)]

def update(ind):

    frame = frames[ind]
    ind += 1
    label.configure(image=frame)
    root.after(5, update, ind)

label = tk.Label(root, fg='blue')
label.pack()

counter_label(label)
root.after(5, update, 0)
root.mainloop()