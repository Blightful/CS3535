"""

Recursively concatenates timbre from hdf5 files in the MSD directory structure.
For example:
$ python all_pitches_msd.py /u/classes/3535/modules/MillionSongSubset/data/

Based on all_pitches_msd.py code by Mitch Parry 2015-02-12

code for finding timbre and saving to pickle by Walt Scarboro
"""

import cPickle as pickle
    except ImportError:
        import pickle

import sys
import os
import hdf5_getters
import numpy as np

def _is_hdf5(f):
    _, ext = os.path.splitext(f)
    ext = ext[1:] # drop leading '.'
    return ext == 'h5'

def _get_one_timbre(f):
    with hdf5_getters.open_h5_file_read(f) as h5:
        timbre = hdf5_getters.get_segments_timbre(h5)
        return timbre

def get_all_timbre(directory):
    "get the pitches for each hdf5 file in this or any subdirectories"
    timbre = []
    for f in os.listdir(directory):
        path = os.path.join(directory, f)
        print path
        if _is_hdf5(f):
            p = _get_one_timbre(path)
            """
            Right here is where I'd start making pickle saves of the arrays "p" which represent the timbre values for 1 song,
            I also have a choice of making a GMM and pickling that for a given song. A helper method will be called here because the operations on
            these arrays will be quite extensive. Look to my second research module for updated and completed source code or look to my first research module
            to learn how I determine timbre similarity values and GMM's for 2 songs at a time.
            """
            timbre.extend(p)
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