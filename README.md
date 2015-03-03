# CS3535
echonest testing

WINDOWS REMIX INSTALLATION WORK AROUND
###########################################################################
If anyone is still having trouble with getting the remix modules for Windows
I found a really easy way to do it IF you have github working (or can WinSCP from student). 
Instead of just using git to pick up the examples you can use it to take the entire remix repository 
(or just remix/external/). Inside the external folder are all the modules that are used alongside things in remix 
and you can use the setup in their respective folders for each of these modules with "python setup.py install" 
that will automatically add it to your path. I got dirac and cAction this way and now I can run the examples 
(pysoundtouch is also in here and is important for other things). 


Steps (inside wherever you want to save these files for now):

git clone https://github.com/echonest/remix.git

git submodule update --init

cd to remix/external/

cd into module that you need

inside module folder: python setup.py install

------------------------------------------------------------------------

there is a setup for the entire directory but the way its setup causes a lot of problems and errors. 
copying remix/src/ from the git install and adding it to my path manually was the easiest fix for that. 