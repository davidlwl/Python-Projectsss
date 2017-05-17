import os
import string
import time
import shutil
#autobackup phone photos whenever plugged in
###################################################
__SRCDIR__ = r""
__DESTDIR__ = r""
###################################################
'''
sdatetime = time.strftime("%y%m%d")
os.makedirs(__DESTDIR__ + '/' + sdatetime)'''

for arg, dirname, files in os.walk(__SRCDIR__, topdown=False):
    for name in files:
        if name[-3:].lower() in ("mov",'png','gif', 'txt'):
            srcfile = r"%s\%s" % (arg, name)
            print(srcfile)
            destfile = r"%s\%s" % (__DESTDIR__, name)
            print (destfile)
            shutil.copyfile( srcfile, destfile)
              
###################################################

