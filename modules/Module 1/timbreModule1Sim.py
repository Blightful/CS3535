
"""
Author: Walt Scarboro
Finds timbre similarity for 2 given mp3 based on the probability that data from
one song will fall within the model for the other given song.

#CURRENTLY NEEDS TUNING TO BE ABLE TO DISPLAY SIMILARITY IN MEANINGFUL MANNER#
##############CURRENT VALUES MUST BE SORTED AGAINST OTHER VALUES##############


"""

import math

import pyechonest
import echonest.remix.audio as audio
import numpy
from sklearn import mixture

# similarity = 0.002407
audio_file = audio.LocalAudioFile('Eleanor Rigby.mp3')
# audio_file = audio.LocalAudioFile('Romance2.mp3') 
audio_file2 = audio.LocalAudioFile('Romance2.mp3')


timbre = audio_file.analysis.segments.timbre
timbre2 = audio_file2.analysis.segments.timbre

a = numpy.array(timbre)
b = numpy.array(timbre2)

lenA = len(a)
lenB = len(b)
print 'Song 1, number of segments: ' + str(lenA)
print 'Song 2, number of segments: ' + str(lenB)





numpy.random.seed(1)

modelA = mixture.GMM(n_components=3, covariance_type='diag', random_state=None,
 thresh=0.01, min_covar=0.001, n_iter=1000, n_init=1, params='wmc',
  init_params='wmc')


modelB = mixture.GMM(n_components=3, covariance_type='diag', random_state=None,
 thresh=0.01, min_covar=0.001, n_iter=1000, n_init=1, params='wmc',
  init_params='wmc')


modelA.fit(a)
modelB.fit(b)




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


print valAb
print valAa
print valBa
print valBb

prob = (valAb - valAa)/(2.00 * lenA) + (valBa - valBb)/(2.00 * lenB)

print prob
print math.exp(prob)



		