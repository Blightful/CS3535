timbreSim


PROBLEM
############
I wanted to find the similarity between 2 songs based on their timbre
values for an input audio file. The goal is to be able to find similar songs 
given only their audio files or representation.

PROCESS
##############
My code is a fairly simple script that takes two strings that represent audio files
within the same directory as the '.py' file. It does this by using Gaussian Mixture Models and their scores to create a representation of any given segments probability to be found within the songs data. 

Each length 12 array of timbre is simplified into score values (1 per segment) that represent the probability that a given point will be successfully fitted to the entire song. By getting this information for two different songs (in this example) and comparing the two against each other, you can find the relative timbre similarity for the two songs.

Because the data was initially too small, the models had to be averaged rather than summed to create a value other than 0 (results were too far in the negatives to be brought back to beyond zero)

DEPENDENCIES
#############

echonest.remix.audio

pyechonest

sklearn.mixture (available through scikit-learn)

numpy