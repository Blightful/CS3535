PROBLEM
##########
I want to represent, sort, analyze, and/or visualize songs in a useful fashion.

QUESTION
##########
1. What do the self-similarity graphics actually represent?
2. How plausible is "Islands of Music" on the per song basis? (SOM)
3. How do you uniquely represent a song?


RESOURCES
##########
1. http://www.fxpal.com/publications/visualizing-musical-structure-and-rhythm-via-self-similarity.pdf 

2. http://www.ofai.at/~elias.pampalk/music/pampalk.pdf (More needed on SOM)

3. http://ismir2002.ismir.net/proceedings/02-FP05-2.pdf


NOTES
#########

1. Self-Similarity:

In a self-similarity graph, the color of the diagonal that runs from bottom-left to top-right is the color of highest similarity. Colors opposite to your similar color are disimilar. Checkerboards are repeating motifs for similar sections of audio. Presenting useful visual representations of data similar to this one is important for finding which audio measure or attribute is most impactful in similarity between 2 or more songs.


2. Islands of music:

The idea behind this is that music can be sorted visually and algorithmically into clusters based on some given similarity. This idea is achieved mostly by Self-Organizing Maps; from the thesis, "The goal of clustering data is to find groups (clusters) of data items that are similar to each other and different from the rest of the dataset." From what I gathered, it should be possible to create a mapping of songs with each data point on a map representing a different song and the proximity of the dots representing their similarity. Two issues I forsee are the size of the memory needed for calculations, and generating a descriptor that can be represented in 2D or 3D space. 



3. Multi-song similarity:

Timbre seems to be one of the generally accepted ways of finding music similarity. The article goes on to explain that a lot of the similarities generated could be found simply in the meta data, but it also found unexpected similarities from the AudioQuantum data that could be used to group songs based on similar timbre/sound. When referenced against different filters this method could be used to generate playlists within a threshold of similarity from a larger dataset of music. I should investigate timbre in conjunction with other descriptors for mapping the songs into "islands."