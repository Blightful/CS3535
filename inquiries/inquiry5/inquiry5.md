### PROBLEM

My timbre build and compare programs aren't very user friendly or overly useful. This weeks work is on adding more ways to search for songs (local audio) and a return that can be sorted and read (pprint) by an average user.

Another problem where other songs are coming up as more similar than a different upload of the same song. For example, a Tom Petty song showed up as th 16th most similar out of 294 when I uploaded a youtube rip of the same song. It is possible that a different version was used for the HDF5 file or it could be possible that my program is working incorrectly. The fact that the same song still showed up towards the top of my sorted list leads me to believe that audio quality, song length, and/or echonest timbre extraction are confounding variables to some degree.


### RESOURCES

1. build_gmm_msd.py

2. compare_gmm_msd.py

3. hdf5_getters.py


### NOTES

No new sources were used other than the occassional python documentation. I used my programs that I have been working on all semester and improved upon them during this past week. While making the program easier to use and read was the focus of this week, investigating discrepancies in search results was the second area of focus. 