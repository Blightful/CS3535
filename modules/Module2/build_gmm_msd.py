"""

Recursively pulls timbre from hdf5 files in the MSD directory structure and 
pickles a GMM on the timbre values.

For example:
$ python all_pitches_msd.py /u/classes/3535/modules/MillionSongSubset/data/

Based on all_pitches_msd.py code by Mitch Parry 2015-02-12

code for finding timbre and saving to pickle by Walt Scarboro
"""
try:
    import cPickle as pickle
except ImportError as e:
    import pickle

import sys
import os
import hdf5_getters
import numpy as np
from sklearn import mixture
# import timbreSim

def _is_hdf5(f):
    _, ext = os.path.splitext(f)
    ext = ext[1:] # drop leading '.'
    return ext == 'h5'

def _get_one_timbre(f):
    with hdf5_getters.open_h5_file_read(f) as h5:
        timbre = hdf5_getters.get_segments_timbre(h5)
        return timbre

def _get_one_md5(f):
    with hdf5_getters.open_h5_file_read(f) as h5:
        md5 = hdf5_getters.get_audio_md5(h5)
        return md5

def get_all_timbre(directory):
    "get the timbre for each hdf5 file in this or any subdirectories"
    timbre = []
    for f in os.listdir(directory):
        path = os.path.join(directory, f)
        print path
        if _is_hdf5(f):
            p = _get_one_timbre(path)

            model = mixture.GMM(n_components=3, covariance_type='diag', random_state=None,
            thresh=0.01, min_covar=0.001, n_iter=1000, n_init=1, params='wmc',
            init_params='wmc')

            model.fit(p)

            # md5 = _get_one_md5(path) #Not sure if I'll use this.
            """
            This pickles the model from above as the hdf5 file name concatenated
            with GMM.
            """
            pickle.dump(model, open(str(f[:-3].upper()) + 'GMM' + ".p", 'wb'))
            
        elif os.path.isdir(path):
            p = get_all_timbre(path)
        else:
            continue

        timbre.extend(p)

    return timbre

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'usage: python all_timbre_msd.py path_to_MSD'
    else:
        timbre = get_all_timbre(sys.argv[1])
        #print timbre
        print len(timbre),"total segments"
        print "mean=",np.mean(timbre,axis=0)
        print "stdev=",np.std(timbre,axis=0)