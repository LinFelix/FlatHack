#! /usr/bin/python

from Tkinter import *


class GUI(Frame):

    def add_own_title(self):
        self.ownTitle = Label(master=self.top, underline=0,
                              text="Hackflat \n We show you the apartment you want to see", background="white")
        self.ownTitle.pack()

    def create_top_level(self):
        # the actual window
        self.top = Toplevel(master=self.master)
        self.top.config(background="white", height=1080, width=1920)
        self.top.minsize(width=1920, height=1080)
        self.top.title("FlatHack")

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_top_level()
        self.add_own_title()



if __name__ == '__main__':

    root = Tk()

    gui = GUI(master=root)

    gui.mainloop()
