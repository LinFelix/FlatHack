

from Tkinter import *


class StatusBar(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()


def callback():
    print "called the callback!"

#root = Tk()

# create a toolbar
#toolbar = Frame(root)

#b = Button(toolbar, text="new", width=6, command=callback)
#b.pack(side=LEFT, padx=2, pady=2)

#b = Button(toolbar, text="open", width=6, command=callback)
#b.pack(side=LEFT, padx=2, pady=2)

#toolbar.pack(side=TOP, fill=X)

#status = StatusBar(root)
#status.pack(side=BOTTOM, fill=X)

#mainloop()
