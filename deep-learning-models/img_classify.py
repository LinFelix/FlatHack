# code for extracting the feature matrix of second last or any layer on a pretrained deep neural network on keras

#For installation follow 2 websites :
# 1.  http://www.pyimagesearch.com/2016/08/10/imagenet-classification-with-python-and-keras/
# 2. https://github.com/fchollet/deep-learning-models (code comes from here)
# Comment : takes around 1 min to output the featutes of the last layer so can't process the images of house in real time
# the output matrix is long (1,512,7,7). The outer dimension "1" is dependent on the number of images you want to classify or want features for


from vgg19 import VGG19
from keras.preprocessing import image
from imagenet_utils import preprocess_input
from keras.models import Model
import numpy as np
from imagenet_utils import preprocess_input, decode_predictions
import sys
import os

base_model = VGG19(weights='imagenet')
model = Model(input=base_model.input, output=base_model.get_layer('block5_pool').output)
#model = Model(weights='imagenet')

path="../src/python/GUI/image_retrieval/images/"

print os.listdir(path)

for img_path in os.listdir(path):
	print path+img_path
	img = image.load_img(path+img_path, target_size=(224, 224))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x = preprocess_input(x)

	block5_pool_features = model.predict(x)
	#print block5_pool_features

	tag=img_path.split(".")[0]

	outfile="../src/python/GUI/image_retrieval/features/"+tag+".npy"
	np.save(outfile,block5_pool_features)



