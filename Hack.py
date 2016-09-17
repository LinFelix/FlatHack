from PIL import Image
import numpy as np
import imagehash
import photohash
from imagehash import average_hash
from scipy.ndimage.interpolation import zoom

std_width = 2000
std_height = 2000
Hash = np.full((6), 0, dtype = 'object')

filename = "1.jpeg"
with Image.open(filename) as im:
    width, height = im.size

print std_width/width
print std_height/height

exit()


print width, height
new_image = zoom(filename, (float(std_width/width), float(std_height/height) ), output=None, order=3, mode='constant', cval=0.0, prefilter=True)

exit()
Hash[0] = average_hash(Image.open('1.jpeg'))
Hash[1] = average_hash(Image.open('2.jpeg'))
Hash[2] = average_hash(Image.open('3.jpeg'))
Hash[3] = average_hash(Image.open('4.jpeg'))
Hash[4] = average_hash(Image.open('5.jpeg'))
Hash[5] = average_hash(Image.open('6.jpeg'))


print photohash.hashes_are_similar('1.jpeg', '1.jpeg')
print photohash.hashes_are_similar('1.jpeg', '3.jpeg')
print photohash.hashes_are_similar('1.jpeg', '4.jpeg')
print photohash.hashes_are_similar('1.jpeg', '5.jpeg')
print photohash.hashes_are_similar('1.jpeg', '6.jpeg')
hash_one = average_hash('1.jpeg')
hash_two = average_hash('2.jpeg')
#dist =  photohash.hash_distance(Hash[0], Hash[1])
similar = photohash.is_look_alike('1.jpeg', '2..jpeg', tolerance=3)
print similar
#print dist

print Hash[0]
print Hash[0]-Hash[1]
print Hash[0]-Hash[2]
print Hash[0]-Hash[3]
print Hash[0]-Hash[4]
print Hash[0]-Hash[5]
print Hash.dtype

'''
i = 0
print len(Hash)
for index,val in enumerate(Hash):
	print index+i
	if ((index+i) < len(Hash)):
		print('Difference')
		print (val - Hash[index+i])
		i = i+1

print('End of loop')
print(Hash[0] - Hash[0])
print(Hash[0] - Hash[1])
print(Hash[0] - Hash[2])
print(Hash[0] - Hash[3])
print(Hash[0] - Hash[4])
print(Hash[0] - Hash[5])'''