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

    def create_parameter_request(self):
        self.cityLabel = Label(master=self.top, background="white", height=1, text="Apartment is in: ")
        self.cityLabel.pack()
        self.cityEntry = Entry(master=self.top, background="white")
        self.cityEntry.pack()
        self.priceLabel = Label(master=self.top, background="white", text="The price might range from (CHF)")
        self.priceLabel.pack()
        self.priceMinEntry = Entry(master=self.top, background="white")
        self.priceMinEntry.pack()
        self.priceSeperatorLabel = Label(master=self.top, background="white", text="up to ")
        self.priceSeperatorLabel.pack()
        self.priceMaxEntry = Entry(master=self.top, background="white")
        self.priceMaxEntry.pack()
        self.roomLabel = Label(master=self.top, background="white", text="The apartment has at least")
        self.roomLabel.pack()
        self.roomMinEntry = Entry(master=self.top, background="white")
        self.roomMinEntry.pack()
        self.roomSeperatorLabel = Label(master=self.top, background="white", text="rooms, but no more then")
        self.roomSeperatorLabel.pack()
        self.roomMaxEntry = Entry(master=self.top, background="white")
        self.roomMaxEntry.pack()
        self.confirmationButton = Button(master=self.top, text="I want to SEE apartments",
                                         command=self.collect_user_input())
        self.confirmationButton.pack()

    def collect_user_input(self):
        pass

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_top_level()
        self.add_own_title()
        self.create_parameter_request()


if __name__ == '__main__':

    root = Tk()

    gui = GUI(master=root)

    gui.mainloop()
