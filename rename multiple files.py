import shutil
import os
from os import listdir
from os.path import isfile, join
mypath = 
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in onlyfiles:
    os.rename(mypath+ '/' + file, mypath+ '/' +file[-19:])
    
