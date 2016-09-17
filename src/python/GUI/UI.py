#! /usr/bin/python

from Tkinter import *

import urllib2
import json
import Image
import cStringIO
import photohash
import imagehash
import numpy

from pyimagesearch.rgbhistogram import RGBHistogram
from pyimagesearch.searcher import Searcher
import numpy as np
import argparse
import cPickle
import cv2
import glob

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
                                         command=self.collect_user_input)
        self.confirmationButton.pack()

    def collect_user_input(self):
        self.city = self.cityEntry.get()
        self.minPrice = self.priceMinEntry.get()
        self.maxPrice = self.priceMaxEntry.get()
        self.minRoom = self.roomMinEntry.get()
        self.maxRoom = self.roomMaxEntry.get()
        print(self.city, self.minPrice, self.maxPrice, self.minRoom, self.maxRoom)
        print "first step"

        url = "https://api-2445581357976.apicast.io:443/rs/real-estates?language=en&chooseType=rentflat&"+ \
        "sort=p&page=1&numberResults=1000"+ \
        "&city=Z%C3%BCrich" \
        "&rentFrom="+str(gui.minPrice)+ \
        "&rentTo="+str(gui.maxPrice)+ \
        "&roomsFrom="+str(gui.minRoom)+ \
        "&roomsTo="+str(gui.maxRoom)
        print url

        req = urllib2.Request(url)
        req.add_header("Accept","application/json")
        req.add_header("auth","7567b660d6cf89544516cda0afc63a38")

        r = urllib2.urlopen(req)
        response = r.read()
        data = json.loads(response)

        print "got data"

        flat_cnt = len(data["items"])

        img_cnt = numpy.full((flat_cnt),0,dtype=int)
        for i in range(0,flat_cnt):
            img_cnt[i] = len(data["items"][i]["pictures"])

        hashes = [[] for i in range(flat_cnt)]

        for i in range(0,flat_cnt):
            print "flat: %d" % i
            for j in range(0,img_cnt[i]):
                req_img = urllib2.Request(data["items"][i]["pictures"][j])
                res_img = urllib2.urlopen(req_img)
                img = res_img.read()
                imagefile = open("image_retrieval/images/"+str(i)+"_"+str(j)+".jpg","wb")
                imagefile.write(img)
                imagefile.close()
                file = cStringIO.StringIO(img)
                img = Image.open(file)
                hashes[i].append(int(str(imagehash.average_hash(img)),16))
                print "hash" + " = " + str(hashes[i][j])

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_top_level()
        self.add_own_title()
        self.create_parameter_request()


def mi(i,f):
    return i

def img_sim(f1,i1,f2,i2):
    desc = RGBHistogram([8, 8, 8])
    feat1 = desc.describe(cv2.imread("image_retrieval/images/"+str(f1)+"_"+str(i1)+".jpg"))
    feat2 = desc.describe(cv2.imread("image_retrieval/images/"+str(f2)+"_"+str(i2)+".jpg"))
    (score, imgname) = Searcher(feat1).search(feat2)
    return score

def flat_sim(f1,n1,f2,n2):
    sum=0
    for i in range(0,min(n1,n2)):
        sum=sum+img_sim( f1, mi(i,f1), f2, mi(i,f2) )
    return sum

if __name__ == '__main__':

    root = Tk()

    gui = GUI(master=root)

    gui.mainloop()
