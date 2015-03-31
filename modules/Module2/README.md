What problem does it solve?

Makes optimization of the database into subsets possible and allows for timbre comparisons between any song in the MSD subset.

How did you come up with the idea?

When we first looked into the MSD it became apparent that searching or moving through that amount of data in any reasonable amount of time (for on the fly or real time calculations/queries) would be impossible without a way to reduce the complexity or size of the problem. I knew that reducing the subset into subsets would be a reasonable solution, but at the time I only had the idea of sorting them based on "similarity;" I wasn't really sure what that translated to in terms of music audio data. I looked at every measure of music similarity that was available through echonest (except for beat, tempo, melody; I need a music theorist or someone else for help with that) and decided on timbre as a measure of music similarity. Timbre seemed to be one of the easiest similarities to hear in a song because it makes up the instruments and general "atmosphere" of the song. 

More here maybe

How does it work (what are the key technical contributions)?

1. Finds every HDF5 in the MSD, generates a Gaussian Mixture Model for the timbre values of the song contained within the HDF5, Pickles/cPickles the GMM as "|hdf5filename|GMM.p".  

How can others use it (are there dependencies)?

Others can use it to compare and sort songs by timbre similarity in the MSD. Though the code isn't completed it has all the relevent parts for building the models and comparing them (I will soon (hopefully) put out a revision that allows for command line querying of songs by hdf5 (md5 or song title if I can find a way to make that data more visible in the file structure).

The depencies all seem to be included in the Anaconda distribution; I previously was running a version of PortablePython and it did not include several of the important modules. 

scikit-learn (sklearn) used for mixture models
NumPy
hdf5_getters
and echonest remix


What resources did you use?

http://ismir2002.ismir.net/proceedings/02-FP05-2.pdf

The MSD Subset

HDf5_getters

Something on GMM