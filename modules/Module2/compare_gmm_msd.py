"""

Recursively pulls timbre from hdf5 files in the MSD directory structure and
compares them to the GMM of the other hdf5.

Prints the log 

For example:
$ python all_pitches_msd.py /u/classes/3535/modules/MillionSongSubset/data/

Based on all_pitches_msd.py code by Mitch Parry 2015-02-12

code for finding timbre and saving to pickle by Walt Scarboro
"""
try:
    import cPickle as pickle
except ImportError as e:
    import pickle

from pyechonest import config
config.ECHO_NEST_API_KEY='UV6BRCEQPDZ29OJJ9'
import pyechonest
import echonest.remix.audio as audio

import sys
import os
import hdf5_getters
import numpy as np
from sklearn import mixture
from pprint import pprint
import math
import numpy
# import build_gmm_msd

# queryHDF5 = ""
# queryTimbre = []

def _is_hdf5(f):
    _, ext = os.path.splitext(f)
    ext = ext[1:] # drop leading '.'
    return ext == 'h5'

def _get_one_timbre(f):
    with hdf5_getters.open_h5_file_read(f) as h5:
        timbre = hdf5_getters.get_segments_timbre(h5)
        return timbre

def _get_one_title(f):
    with hdf5_getters.open_h5_file_read(f) as h5:
        title = hdf5_getters.get_title(h5)
        return title

def _get_one_artist(f):
    with hdf5_getters.open_h5_file_read(f) as h5:
        artist = hdf5_getters.get_artist_name(h5)
        return artist

def compare_gmm(g, t, artist, title):
    """
    modelA = queryGMM
    modelB = g

    a = queryTimbre
    b = t
    """
    lenA = len(queryTimbre)
    lenB = len(t)

    scoreAa = queryGMM.score(queryTimbre)
    valAa = 0;
    for pt in range(0, len(scoreAa)):
        valAa += scoreAa[pt]

    scoreAb = g.score(queryTimbre)
    valAb = 0;
    for pt2 in range(0, len(scoreAb)):
        valAb += scoreAb[pt2]


    scoreBa = queryGMM.score(t)
    valBa = 0;
    for pt3 in range(0, len(scoreBa)):
        valBa += scoreBa[pt3]


    scoreBb = g.score(t)
    valBb = 0;
    for pt4 in range(0, len(scoreBb)):
        valBb += scoreBb[pt4]

    prob = (valAb - valAa) + (valBa - valBb)
    probadj = (valAb - valAa)/(2.00 * lenA) + (valBa - valBb)/(2.00 * lenB)

    values_arr = [artist, title, math.exp(probadj)]
    viewer_arr.append(values_arr)

    # print
    # print 'Song similarity         (largest = most similar): ' + str(prob)
    # print 'Song similarity adjusted(largest = most similar): ' + str(math.exp(probadj))
    # print

def get_all_timbre(directory):
    "get the timbre for each hdf5 file in this or any subdirectories"
    timbre = []

    for f in os.listdir(directory):
        path = os.path.join(directory, f)
        # print path
        if _is_hdf5(f):            
            """
            This unpickles the model from above hdf5 file name concatenated
            with GMM. Only works after you have built your GMM 
            """
            gmm = pickle.load(open(str(f[:-3].upper()) + 'GMM' + ".p", 'rb'))
            artist = _get_one_artist(path)
            title = _get_one_title(path)
            timbre = gmm.sample(1000)
            compare_gmm(gmm, timbre, artist, title)
            
        elif os.path.isdir(path):
            p = get_all_timbre(path)
        else:
            continue


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'usage: python compare_gmm_msd.py path_to_MSD'
    else:
        global queryHDF5
        global queryGMM
        global queryTimbre

        global viewer_arr
        viewer_arr = [[None for i in range(3)] for j in range(1)]
        # viewer_arr = [[3]]
        # queryHDF5 = sys.argv[2]
        """
        until querying works for values more simple than HDF5 names just modify the value of below file name.
        """
        

        ###########################################
        # Audio File Local Search
        audio_file = audio.LocalAudioFile('tom petty.mp3')
        timbreA = audio_file.analysis.segments.timbre
        a = numpy.array(timbreA)
        try:
            modelA = mixture.GMM(n_components=10, covariance_type='diag', random_state=None,
            thresh=0.01, min_covar=0.001, n_iter=1000, n_init=1, params='wmc',
            init_params='wmc')
        except Exception as e:
            modelA = mixture.GMM(n_components=7, covariance_type='diag', random_state=None,
            thresh=0.01, min_covar=0.001, n_iter=1000, n_init=1, params='wmc',
            init_params='wmc')
        else:
            modelA = mixture.GMM(n_components=3, covariance_type='diag', random_state=None,
            thresh=0.01, min_covar=0.001, n_iter=1000, n_init=1, params='wmc',
            init_params='wmc')
        modelA.fit(a)

        queryGMM = modelA
        queryTimbre = modelA.sample(1000)
        ##############################################

        # By HDF5 File Name
        # gmm = pickle.load(open('TRAAAAW128F429D538GMM.p', 'rb'))
        # queryGMM = gmm
        # queryTimbre = gmm.sample(10000)

        ###############################################
        get_all_timbre(sys.argv[1])

        arr = sorted(viewer_arr, key=lambda x: x[2], reverse=True)
        pprint(arr)
        
        