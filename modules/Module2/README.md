### What problem does it solve?

Makes optimization of the database into subsets possible and allows for timbre comparisons between any song in the MSD subset.
Also allows for you to find music similar to a user inputted search query.

### How did you come up with the idea?

When we first looked into the MSD it became apparent that searching or moving through that amount of data in any reasonable amount of time (for on the fly or real time calculations/queries) would be impossible without a way to reduce the complexity or size of the problem. I knew that reducing the subset into subsets would be a reasonable solution, but at the time I only had the idea of sorting them based on "similarity;" I wasn't really sure what that translated to in terms of music audio data. I looked at every measure of music similarity that was available through echonest (except for beat, tempo, melody; I need a music theorist or someone else for help with that) and decided on timbre as a measure of music similarity. Timbre seemed to be one of the easiest similarities to hear in a song because it makes up the instruments and general "atmosphere" of the song. This makes it particularly useful for finding music similar to music that you are interested in.

Because the time needed to generate a GMM was just beyond an arbitrary amount of time, I decided that the models could be saved into a pickle file and then easily compared to the timbre values stored in each HDF5.

### How does it work (what are the key technical contributions)?

1. By running build_gmm_msd.py in your hdf5 directory: Finds every HDF5 in the MSD, generates a Gaussian Mixture Model for the timbre values of the song contained within the HDF5, Pickles/cPickles the GMM as "|hdf5filename|GMM.p".
2. By running compare_gmm_msd.py in your hdf5 directory: Finds all GMM pickled files, compares them to a "queried" hdf5gmm, and then outputs the hdf5 file name as a string followed by its similarity to the queried model in 2 different metrics. The adjusted metric is easier to read and is a result of an averaging in a step of the data, but the non-adjusted metric includes the original log scores.

### How can others use it (are there dependencies)?

Others can use it to compare and sort songs by timbre similarity in the MSD. Though the code isn't completed it has all the relevent parts for building the models and comparing them (I will soon (hopefully) put out a revision that allows for command line querying of songs by hdf5 (md5 or song title if I can find a way to make that data more visible in the file structure).

The depencies all seem to be included in the Anaconda distribution; I previously was running a version of PortablePython and it did not include several of the important modules. 

scikit-learn (sklearn) used for mixture models
NumPy
hdf5_getters
and echonest remix


### What resources did you use?

http://ismir2002.ismir.net/proceedings/02-FP05-2.pdf

The MSD Subset

HDf5_getters

http://en.wikipedia.org/wiki/Mixture_model