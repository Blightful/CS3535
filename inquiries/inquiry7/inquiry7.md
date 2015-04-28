## PROBLEM
My program now is capable of doing Local-Local and MSD-MSD comparisons but I'd like the ability to try Local-MSD comparisons. My program also runs slowly and could operate faster with threading and performing multiple processes at once. Included are my python scripts for Local-Local comparisons and operates in much the same way as my database comparison program on a local folder of mp3 (going to make another one for wav to try local-msd comparisons as soon as I can get a large number of wav files).

My two current issues: First, file conversion between MP3 and Wav is likely causing loss of timbre audio data. Second, program searching speed on MSD or Local subsets is slow and could be improved drastically with threading.


## Resources

1. http://www.dievantile.com/2014/11/what-is-the-difference-between-mp3-and-wav-formats/

2. http://developer.echonest.com/forums/thread/32#post89

3. https://developer.echonest.com/forums/thread/155

4. http://web.media.mit.edu/~tristan/

5. https://docs.python.org/2/library/threading.html

## NOTES
1. My first resource is a something I came across when searching for reasons for timbre disparity in local and HDF5 saved audio data. I'm still not certain, but there is evidence that points to a loss in high frequency timbre data when converting from mp3 back to wav. I have been looking in to a way to prove this with search results.

2 & 3.  These are forum posts by Paul Lamere and Tristan Jehan describing timbre and its mechanics in echonest; not all of it was new information but some of the things said about timbre changed how I perceived it and gave me information on what each individual timbre vector represents. Only the first 5 are listed, but I think that there may actually be one vector that I can ignore or alter to fix the disconnect between my local audio files and the database. 

4. This is Tristan Jehan's homepage. I went through all of his material on timbre and there are actually several articles. I haven't finished reading all of them but from what I have read, this guy knows way too much about music.

5. I only started studying up on threading, I haven't actually implemented it or fully understand it yet. It looks like it will be as simple as adding an extra layer of code into one of my loops in build and compare. My compare program was only a few minutes run time originally but all the changes I made to it over the semester slowed it to ~15-20 minutes (albeit with much more accurate results); with threading I hope to be able to get it back to a reasonable run time. 