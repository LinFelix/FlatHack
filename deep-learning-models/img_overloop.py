from vgg19 import VGG19
from keras.preprocessing import image
from imagenet_utils import preprocess_input
from keras.models import Model
import numpy as np
from imagenet_utils import preprocess_input, decode_predictions
import sys
from os import walk

base_model = VGG19(weights='imagenet')
model = Model(input=base_model.input, output=base_model.get_layer('block5_pool').output)
#model = Model(weights='imagenet')


a = [];
for (dirpath, dirnames, filenames) in walk('../src/python/GUI/image_retrieval/images'):
    a.extend(filenames)
    break

for i in a:
	img = image.load_img('../src/python/GUI/image_retrieval/images/'+i, target_size=(224, 224))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x = preprocess_input(x)

	block5_pool_features = model.predict(x)
	print block5_pool_features

	f = open("feature.txt", "w")
	f.write(str(block5_pool_features))




	
