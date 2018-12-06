import tkinter
import PIL.Image
import PIL.ImageTk


main = tkinter.Tk(className="#Tetris")

logo = tkinter.PhotoImage(file='tetrisCover.png')

label = tkinter.Label(main, compound = tkinter.CENTER, image = logo)
label.pack()
mframe = tkinter.Frame(main)
mframe.pack()

def clearwin(event=None):
    '''Clear the main windows frame of all widgets'''
    for child in mframe.winfo_children():
        child.destroy()

def win1(event=None):
    '''Create the main window'''
    clearwin()
    b1 = tkinter.Button(mframe, command=win2, text='Start Game')
    b1.pack()
    b2 = tkinter.Button(mframe, command=win3, text='Options')
    b2.pack()

def win2(event=None):
    '''Create the second sub window'''
    clearwin()
    if __name__ == '__main__':
	    App = TetrisApp()
	    App.run()
   
    #entry1 = tkinter.Entry(mframe)
    #entry1.pack()
    #back = tkinter.Button(mframe, command=win1, text='Quit')
    #back.pack()

def win3(event=None):
    '''Create the third sub window'''
    clearwin()
    label1 = tkinter.Label(mframe, text='Settings')
    label1.pack()
    back = tkinter.Button(mframe, command=win1, text='Back')
    back.pack()

win1()

main.mainloop()