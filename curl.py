import urllib2
import json
import Image
import cStringIO

req = urllib2.Request("https://api-2445581357976.apicast.io:443/rs/real-estates?language=en&chooseType=rentflat&sort=p&page=1&numberResults=10&zip=8052&rentFrom=1500&rentTo=2000&roomsFrom=3&roomsTo=4")
req.add_header("Accept","application/json")
req.add_header("auth","7567b660d6cf89544516cda0afc63a38")

r = urllib2.urlopen(req)

response = r.read()

data = json.loads(response)

for pic in data["items"][2]["pictures"]:
	req_img = urllib2.Request(pic)
	res_img = urllib2.urlopen(req_img)
	img = res_img.read()
	file = cStringIO.StringIO(img)
	Image.open(file).show()

