PROBLEM
##########
I want to expand my timbre similarity program to the Million Song Database (MSD). 

QUESTION
##########
1. What can I learn from Dr. Parry's inquiry into pitches for the MSD in relation to my problem?
2. How will I deal with the large amount of time spent calculating and creating timbre arrays for every song in the database multiple times?
3. What am I actually comparing?


RESOURCES
##########
1. https://github.com/rmparry7/echonest/tree/master/all_pitches_msd

2. https://docs.python.org/2/library/pickle.html#pickling-and-unpickling-external-objects

3. http://www.indiana.edu/~emusic/etext/acoustics/chapter1_timbre.shtml


NOTES
#########

1. ALL PITCHES MSD -> ALL TIMBRE + GMM MSD

Converting Dr. Parry's all_pitches_msd.py file into one for timbre was incredibly easy; it only involved changing pitches -> timbre in most cases. I'll need to make a helper method with my timbre similarity code to generate GMM for each of these timbre arrays. Ideally I want to be able to generate a folder, separate the hdf5, containing all of the song timbre arrays and/or the Gaussian Mixture Model (GMM) for each array.
For more info on hdf5 getters you can look at Parry's examples, or line 39 in all_timbre_msd.py for my notes as well as the relevant code for accessing individual arrays.

2. USING PICKLE TO STORE MODELS OR TIMBRE ARRAYS

When I looked into storing arrays I found a python library with the explicit purpose of storing objects, Pickle. Pickle is actually incredibly simple and the resource link directs to a tutorial.
Being able to generate 10K Pickle files is pretty much useless unless they can be named in such a way that they can be queried externally; for this I found the attribute "persistent_ID" which will allow me to name the files after their md5 or song/artist name concatenation. Another thing worth investigating is cPickle, which can use lists as persistent_ID's within a pickle file; being able to pickle all the arrays into one file COULD be used if I figure out to uniquely name arrays (arrayX[0] == song/artist/MD5?).

3. WHAT IS TIMBRE?

Timbre is described as being closely related to the "spectral envelope." It's the cue in your brain that differentiates between the same note played on different intruments.
Some songs are clearly dominated by instruments and those instruments and the level of distortion/alteration done to those instruments generally are the variables driving the change in timbre values for a song.
For example Eleanor Rigby by the Beatles brings up several other violin driven songs when queried for timbre similarity. 
I had to look up what timbre meant when I first investigated it, but realized I didnt really understand what it was trying to explain. The site in resource 3 is an online textbook for acoustics and gives pretty good
simplified explanations for a lot of the music concepts in class. This is a decent resource in general.