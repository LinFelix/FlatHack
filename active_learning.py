# code for active bayesian based learning 

import numpy as np

# Initialization 
flats_seen = 0 # id of the flat seen, 0 as the first flat is seen/proposed first in initialization
sum = np.full((len(flat_cnt),0, dtype = 'float'))
 # sum of all similarities
iteration_count = 1
flat_score = np.full((len(flat_cnt),0, dtype = 'float'))

proposed_flat = 0 # the first flat is proposed as no prior knowledge

updated_score = np.full((len(flat_cnt),0, dtype = 'float'))
iteration_count += 1

print('User please enter if you liked the proposed flat.')
user_rating = input('Enter +1 for :) and -1 for :(') # Take the input from user and store it in variable user_rating

while (len(flats_seen) != len(flat_cnt)): # *** insert condition such that loop stops after every flat in the set has been seen
	# insert function that returns sum and flat_sim (flat_similarity vector) here
	n1 =  # number of images in flat 1
	n2 =  # number of images in flat 2
	f1 =  # flat score of flat 1
	f2 =  # flat score of flat 2 

	updated_score = update_score(flat_score, proposed_flat, user_rating, sum, flat_sim)

	# propose the next flat as one that has highest score and has not been proposed before
	proposed_flat = np.where(updated_score == updated_score.max())
	flats_seen = np.append(flats_seen, proposed_flat)

def mi(i,f): # i is the identifier (bathroom/living room ....)
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

# function for updating scores
def updated_score(flat_score, proposed_flat, user_rating, sum, flat_sim):

	for i in range(0,len(flat_cnt)):
		if iteration_count == 1:
			flat_score[i] = user_rating * flat_sim[0]  # flat_sim is the vector that shows similatrity between flats
		else :
			flat_score[i] = ((user_rating*flat_sim[proposed_flat]) + flat_score[i])/(sum)

	return flat_score

