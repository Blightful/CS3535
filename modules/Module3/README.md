### What problem does it solve?

Can solve the issue with finding paths through similar song sets. The code included with this module is my updated build_gmm_msd.py and compare_gmm_msd.py that are built to run on the MSD or MSD10k. Unfortunately my new program for generating graphs and/or edges for song similarity to map them together isnt done. I don't think this new program iteration will be my final project but it is likely to be the start of it. If my new program works at making pathways between large song sets in any kind of reasonable amount of time, I should be able to make the PlaylistPlayer do some interesting things. 

### How did you come up with the idea?

Dr. Parry helped me piece it together, but the idea of creating a path through a set of songs based on timbre similarity has been an idea I have played around with since I came up with my similarity program. The idea is to generate a path that finds the most similar songs to a given song (say 10 or so) and follows it through and finds the most similar matches for those songs. The idea here is to build a type of graph that can map the songs and find different paths that either hit every song or only songs above a certain similarity threshold. 


### Some observations on the theory and results
From my experimentation, I've found that songs with similarity thresholds higher than 0.2 on my scale have had noticeably similar timbre and I'd probably use that as my threshold. 

I also noticed that when you compare MP3's to HDF5 GMM's you get very different results than HDF5's to HDF5's (even when using the same song). MP3 based queries have a much lower similarity measure's overall; the top results for mp3 based queries will rarely pass 0.1 and often extend to 10^-30 or so on the bottom of the range. 

When I made the comparison based on random HDF5's it would always find itself as a perfect match at the top of the results and would list the other matches below; the difference here is that the HDF5 based queries would return a handful above 0.2 (usually) and even the worst case in the top 50 doesn't go beyond 10^-(2 or so).

On my original project using only MP3 to MP3 comparisons I got results on a similar scale to the HDF5 on HDF5 queries. This new edge building program is going to likely run only on MP3's, so I should be able to test my theory on a larger sample size (8000 rather than 5). 

The fact that my similarity measure between MP3 and HDF5 are much less comparable and produce more varied results leads me to believe that the download/creation source of MP3's and the version of echonest that the HDF5's were built on, are to some degree important factors. 

Lastly, complexity. I can make this code more efficient and I plan on optimizing the code, as well as, implementing some parallel processing/threading in my final project.


### How can others use it (are there dependencies)?

Others can use it to compare and sort songs by timbre similarity in the MSD.
Right now it takes an HDF5 or Local MP3 and returns a sorted list of tuples that have Artist, Song title, and Similarity measure.  

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