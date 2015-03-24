PROBLEM
##########
I am still looking into expanding timbre similarity to a dataset of songs, but I am also looking into other methods of music similarity and hope to create a more robust
music similarity search algorithm. The goal is to work towards my final project, which I planning on doing in the area of similarity analysis for large datasets; I hope to be able to enter in a series of parameters
that return a sorted list of song identifiers. If all goes well, I should be able to use my code for building subsets (?) within the MSD that will allow for quicker and more accurate transitions in the Jukebox/Infinite playlister. 

Values that I have looked into currently: Valence, Energy, *Acousticness (not as much focus here, seems better as a filter on subsets and doesn't give much different than what timbre tells you).

Values that I am researching for importance: Beat/tempo matching (most likely/highest priority), pitch (as opposed to timbre), loudness (not sure if timbre accounts for this, check)  

Research done this week is fairly similar to last week and most of the progress has been in working on my code. Progress since last report: can generate pickle files and name them (not finalized on naming convention), can query based on MD5 (would like to support by title and artist through echonest lookup), and I've tried making small scripts for testing out other attributes effectiveness (nothing super interesting or conclusive but there at least appears to be a correlation; beat-matching on subsets is what I WANT to test whenever I can finish my timbre code).

QUESTION
##########
1. What attributes in echonest can be supplemented or used as a filter in my querying program?
2. SOM on MSD using Timbre? (still unanswered, need to finish my code)


RESOURCES
##########
1. http://blog.echonest.com/post/66097438564/plotting-musics-emotional-valence-1950-2013 (one of many blogs, I read nearly all of them relating to audio data/attributes)
http://developer.echonest.com/acoustic-attributes.html for descriptions

2. SOM assignment, http://asulearn.appstate.edu/pluginfile.php/1135470/mod_resource/content/0/Music%20Visualization.pdf


NOTES
#########

1. VALENCE AND OTHER ATTRIBUTES IN ECHONEST

The article I linked is just the article on tracking Valence of music over time, but it has links to several other articles and the blog itself contains other articles. 
In the indicated article, however, it indicates that the average valence for music has been on a slight decline since the 50's. When you look at the hits over those years or if you consider the style of music that was popular in the 50's-60's, you could see how valence would be higher during that time and the type of feel good music that it represents. For example: low valence/high energy = angry, low energy/low valence = sad, high energy/high valence = delighted or happy, etc. Link below has a chart, it is only relative and doesn't have values however.
Also a bonus, Paul Lamere posts on the echonest forums and had this to say about Valence and Energy http://developer.echonest.com/forums/thread/1297. When using valence and energy in conjunction, the theory is that you can get a mood from the song and that mood translates well in to some qualifier. I think valence and energy has potential to "replace" my timbre search, but I dont need to. It's worth investigating which performs better, however.

2. ORGANIZING THE MSD INTO SUBSETS USING TIMBRE SIMILARITY AS COMPLEXITY REDUCTION

I haven't gotten to look as far as I wanted into this, but the SOM assignment that we have been working on for the past week shows me that my concept is at least "possible." We organized major and minor triads based on similarity to each other, but what I'm wondering is the size of these subsets within the MSD and what control I will have over their construction. The assignment allowed us access enough to find and identify the major and minor triads within the map; so, my plan is to break the MSD into small enough subsets that an infinite jukebox on a subset could perform significantly more accurately and quickly than on the full dataset. While my understanding of SOM is still not as in depth as I would hope, I've already seen that the necessity for these subsets does exist and that SOM has potential to be the solution.

