### Progress from (4-9-15 - 4-14-15)
Not much was done since the last inquiry report. 
1. Fixed bugs for running my code on the subset without errors.
   Issues with different sized datasets meant that different tiers of precision with try-except blocks were necessary for the build_gmm_msd to run on the MSD10k dataset without error.

2. Built the GMM subset for the 10K song subset.
   After building the GMM subset I was able to test queries on larger datasets and my focus is tuning my code to make it more accurate. I may need to change my base similarity algorithm significantly. When querying a youtube rip of a song that is in the database it doesn't show up in the top 50, but the songs towards the top of the list are emperically more similar than songs that show up towards the bottom. That is, in most cases; some songs dont pick up very good results and I need to look in to that just through testing it and listening to results. It seems like songs with a focus on instrumentals pull in better results and if that is the case, making the algorithm better may be very difficult.

3. I have a theory currently that vocals and song length (or how echonest gets timbre values) are where the issue is coming from. You can easily spot similarities in the songs it returns but it seems the numbers don't mean all that much and similarity can still be found further down in the top portion of the list. 

# Looking Forward
I need to focus on making sure that the algorithm my code is built on, will, in fact, work. At the very least it needs to refined. If I want to optimize a database with my working code, I need to look into a naming convention or file structure that will make grouping by timbre similarity possible. 

I should also make sure that sampling rather than using data from the actual timbre arrays is not the problem. Making that code run in any reasonable time is the hard part. My build_gmm program took ~30 minutes on the 10K subset and search queries with compare_gmm take about a minute (not THAT bad, but 100 minutes on 1million songs is).