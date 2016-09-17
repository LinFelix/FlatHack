#! /usr/bin/python

from Tkinter import *

import urllib2
import json
from PIL import Image
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

def mi(i,f):
    return i

def img_dis(f1,i1,f2,i2):
    index = {}
    desc = RGBHistogram([8, 8, 8])
    path1 = "image_retrieval/images/"+str(f1)+"_"+str(i1)+".jpg"
    feat1 = desc.describe(cv2.imread(path1))
    feat2 = desc.describe(cv2.imread("image_retrieval/images/"+str(f2)+"_"+str(i2)+".jpg"))
    index[path1] = feat1
    results = Searcher(index).search(feat2)
    return results[0][0]

def flat_dis(f1,n1,f2,n2):
    sum=0
    for i in range(0,min(n1,n2)):
        sum=sum+img_dis( f1, mi(i,f1), f2, mi(i,f2) )
    return sum

# function for updating scores
def update_score(flat_score, proposed_flat, flat, user_rating, img_cnt):
    dis = flat_dis( proposed_flat, img_cnt[proposed_flat],  flat, img_cnt[flat])
    return flat_score + user_rating*np.exp(-0.1*dis)


class GUI(Frame):

    def add_own_title(self):
        self.ownTitle = Label(master=self.top, underline=0,
                              text="Hackflat \n We show you the apartment you want to see", background="white")
        self.ownTitle.pack()

    def refresh_pic(self,path1,path2,path3):
        pass

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

        url = "https://api-2445581357976.apicast.io:443/rs/real-estates?language=en&chooseType=rentflat&"+ \
        "sort=p&page=1&numberResults=1000"+ \
        "&city=Z%C3%BCrich" \
        "&rentFrom="+str(gui.minPrice)+ \
        "&rentTo="+str(gui.maxPrice)+ \
        "&roomsFrom="+str(gui.minRoom)+ \
        "&roomsTo="+str(gui.maxRoom)

        req = urllib2.Request(url)
        req.add_header("Accept","application/json")
        req.add_header("auth","7567b660d6cf89544516cda0afc63a38")

        r = urllib2.urlopen(req)
        response = r.read()
        data = json.loads(response)

        flat_cnt = len(data["items"])

        img_cnt = numpy.full(flat_cnt,0,dtype=int)
        for i in range(0,flat_cnt):
            img_cnt[i] = len(data["items"][i]["pictures"])
        '''
        zcnt=0
        for i in range(0,flat_cnt):
            if(img_cnt[i]!=0):
                print "flat: %d" % (i-zcnt)
                for j in range(0,img_cnt[i]):
                    req_img = urllib2.Request(data["items"][i]["pictures"][j])
                    res_img = urllib2.urlopen(req_img)
                    img = res_img.read()
                    imagefile = open("image_retrieval/images/"+str(i-zcnt)+"_"+str(j)+".jpg","wb")
                    imagefile.write(img)
                    imagefile.close()
                    file = cStringIO.StringIO(img)
                    img = Image.open(file)
                print str(i-zcnt)+"_"+str(j)
            else:
                zcnt=zcnt+1
        '''
        flat_cnt = numpy.count_nonzero(img_cnt)
        img_cnt = np.delete(img_cnt,np.where(img_cnt==0))

        # Initialization 
        flats_seen = [] # id of the flat seen, 0 as the first flat is seen/proposed first in initialization
         # sum of all similarities
        flat_score = np.full(flat_cnt,0, dtype = 'float')
        proposed_flat = 0 # the first flat is proposed as no prior knowledge

        print('User please enter if you liked the proposed flat.')
        user_rating = input('Enter +1 for :) and -1 for :(') # Take the input from user and store it in variable user_rating

        while (len(flats_seen) != flat_cnt): # *** insert condition such that loop stops after every flat in the set has been seen
            # insert function that returns sum and flat_sim (flat_similarity vector) here
            for f in range(0,flat_cnt):
                flat_score[f] = update_score(flat_score[f], proposed_flat, f, user_rating, img_cnt)

            # propose the next flat as one that has highest score and has not been proposed before
            flats_seen = np.append(flats_seen, proposed_flat)
            tmp_flat_score = np.copy(flat_score)
            tmp_flat_score[flats_seen.astype(int)] = -2
            proposed_flat = np.where( tmp_flat_score == tmp_flat_score.max() )[0][0]


            print('User please enter if you liked the proposed flat.')
            user_rating = input('Enter +1 for :) and -1 for :(')

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_top_level()
        self.add_own_title()
        self.create_parameter_request()

# MAIN #########

if __name__ == '__main__':

    root = Tk()

    gui = GUI(master=root)

    gui.mainloop()
