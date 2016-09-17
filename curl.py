import urllib2
import urllib
import json
import Image
import cStringIO
import photohash
import imagehash
import numpy

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
		urllib.urlretrieve(data["items"][i]["pictures"][j],"/image_retrieval/images/"+str(i)+"_"+str(j)+".jpg")
		req_img = urllib2.Request(data["items"][i]["pictures"][j])
		res_img = urllib2.urlopen(req_img)
		img = res_img.read()
		file = cStringIO.StringIO(img)
		img = Image.open(file)
		hashes[i].append(int(str(imagehash.average_hash(img)),16))
		print "hash" + " = " + str(hashes[i][j])