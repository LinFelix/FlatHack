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



req = urllib2.Request("https://api-2445581357976.apicast.io:443/rs/real-estates?language=en&chooseType=rentflat&sort=p&page=1&numberResults=10&zip=8052&rentFrom=1500&rentTo=2000&roomsFrom=3&roomsTo=4")
req.add_header("Accept","application/json")
req.add_header("auth","7567b660d6cf89544516cda0afc63a38")

r = urllib2.urlopen(req)
response = r.read()
data = json.loads(response)


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
