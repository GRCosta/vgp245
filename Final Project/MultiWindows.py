import tkinter as tk
from tkinter import *
import os
import pygame
import PIL.Image
import PIL.ImageTk
import SimpleTetris

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.logo = tk.PhotoImage(file='tetrisCover.png')
        self.label = tk.Label(self.master, compound = tk.CENTER, image = self.logo)
        self.button1 = tk.Button(self.frame, text = 'Start Game', width = 25, command = self.StartGame)
        self.label.pack()
        self.button1.pack()
        self.frame.pack()

    def StartGame(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = GameScreen(self.newWindow)

class GameScreen:
    def __init__(self, master):
        self.master = master
        
        self.embed = tk.Frame(self.master, width = 500, height = 500) #creates embed frame for pygame window
        self.embed.grid(columnspan = (600), rowspan = 500) # Adds grid
        self.embed.pack(side = LEFT) #packs window to the left

        self.buttonwin = tk.Frame(self.master, width = 75, height = 500)
        self.buttonwin.pack(side = LEFT)        
        
        os.environ['SDL_WINDOWID'] = str(self.embed.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        
        self.screen = pygame.display.set_mode((500,500))
        self.screen.fill(pygame.Color(255,255,255))

        pygame.display.init()
        pygame.display.update()

        def draw():
            pygame.draw.circle(self.screen, (0,0,0), (250,250), 125)
            pygame.display.update()


        self.button1 = Button(self.buttonwin,text = 'Draw',  command=draw)
        self.button1.pack(side=LEFT)
        self.master.update()



        self.quitButton = tk.Button(self.master, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()


    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk(className=" Tetris")

    app = MainMenu(root)
    root.mainloop()


def Tetris():
    rootTetris = tk.Tk(className=" Tetris")    

    app = GameScreen(rootTetris)
    rootTetris.mainloop()

if __name__ == '__main__':
    main()