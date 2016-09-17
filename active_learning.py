# code for active bayesian based learning 

import numpy as np

# Initialization 
flats_seen = [] # id of the flat seen, 0 as the first flat is seen/proposed first in initialization
sum = np.full((len(flat_cnt),0, dtype = 'float'))
 # sum of all similarities
iteration_count = 1
flat_score = np.full((len(flat_cnt),0, dtype = 'float'))

proposed_flat = 0 # the first flat is proposed as no prior knowledge

flat_score = np.full((len(flat_cnt),0, dtype = 'float'))
iteration_count += 1

print('User please enter if you liked the proposed flat.')
user_rating = input('Enter +1 for :) and -1 for :(') # Take the input from user and store it in variable user_rating

while (len(flats_seen) != flat_cnt): # *** insert condition such that loop stops after every flat in the set has been seen
	# insert function that returns sum and flat_sim (flat_similarity vector) here
	for f in range(0,flat_cnt):
		flat_score[f] = update_score(flat_score[f], proposed_flat, f, user_rating, sum[f])

	# propose the next flat as one that has highest score and has not been proposed before
	flats_seen = np.append(flats_seen, proposed_flat)
	tmp_flat_score = flat_score
	tmp_flat_score[flats_seen] = -2 
	proposed_flat = np.where( tmp_flat_score == flat_score.max() )

	print('User please enter if you liked the proposed flat.')
	user_rating = input('Enter +1 for :) and -1 for :(')

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
def update_score(flat_score, proposed_flat, flat, user_rating, sum):
	sim = flat_sim( proposed_flat, img_cnt[proposed_flat],  flat, img_cnt[flat])
	return ( flat_score + user_rating*sim ) / (sum + sim)

