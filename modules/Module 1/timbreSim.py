
"""
Author: Walt Scarboro
Finds timbre similarity for 2 given mp3 based on the probability that data from
one song will fall within the model for the other given song.

#CURRENTLY NEEDS TUNING TO BE ABLE TO DISPLAY SIMILARITY IN MEANINGFUL MANNER#
##############CURRENT VALUES MUST BE SORTED AGAINST OTHER VALUES##############

Output values closer to 0 are more dissimilar.

"""

import math

import pyechonest
import echonest.remix.audio as audio
import numpy
from sklearn import mixture

"""
These are the two MP3's I used and the value that was outputted.
Here I used Eleanor Rigby by The Beatles and Romance No.2 by Beethoven for the 
similar sounding violin and sound. 

For you own local audio files, simply change out the below MP3's for you own local files.
"""
# similarity = 0.002407
audio_file = audio.LocalAudioFile('Eleanor Rigby.mp3')
# audio_file = audio.LocalAudioFile('Romance2.mp3') 
audio_file2 = audio.LocalAudioFile('Romance2.mp3')



"""
This is extracting the timbre into 2 separate 2D arrays and then 
saving as a numpy array object of names a and b.
"""
timbre = audio_file.analysis.segments.timbre
timbre2 = audio_file2.analysis.segments.timbre

a = numpy.array(timbre)
b = numpy.array(timbre2)

lenA = len(a)
lenB = len(b)
print 'Song 1, number of segments: ' + str(lenA)
print 'Song 2, number of segments: ' + str(lenB)



"""
Here I generate the models big A/B to compare to the timbre data sets a/b
Comparisons between Aa, Ab, Ba, and Bb are generated.
"""
modelA = mixture.GMM(n_components=3, covariance_type='diag', random_state=None,
 thresh=0.01, min_covar=0.001, n_iter=1000, n_init=1, params='wmc',
  init_params='wmc')


modelB = mixture.GMM(n_components=3, covariance_type='diag', random_state=None,
 thresh=0.01, min_covar=0.001, n_iter=1000, n_init=1, params='wmc',
  init_params='wmc')


modelA.fit(a)
modelB.fit(b)



"""
This creates a score representing the data a/b projected on the model A/B and 
sums the score array into a single value. Because the values are log scores, they are
all fairly negative and generate fairly large negative numbers. Issue addressed further 
down[*]
"""
scoreAa = modelA.score(a)
valAa = 0;
for pt in range(0, len(scoreAa)):
	valAa += scoreAa[pt]

scoreAb = modelB.score(a)
valAb = 0;
for pt2 in range(0, len(scoreAb)):
	valAb += scoreAb[pt2]


scoreBa = modelA.score(b)
valBa = 0;
for pt3 in range(0, len(scoreBa)):
	valBa += scoreBa[pt3]


scoreBb = modelB.score(b)
valBb = 0;
for pt4 in range(0, len(scoreBb)):
	valBb += scoreBb[pt4]


print "Model B on timbre data a: " + str(valAb)
print "Model A on timbre data a: " + str(valAa)
print "Model A on timbre data b: " + str(valBa)
print "Model B on timbre data b: " + str(valBb)

"""
[*]: lenA and lenB here represent the number of segments in the respective song data.
Here they are used to average the summed scores "val'Xx'"

This step is necessary because without averaging them, the negative values, that you can
see in the output would be too large and the math.exp(prob) would only be capable of producing
0's. 
"""
prob = (valAb - valAa)/(2.00 * lenA) + (valBa - valBb)/(2.00 * lenB)

#print prob
print 'Song similarity: ' + str(math.exp(prob))



		