import os
import shutil

path = r''
list_ = os.listdir(path)


for file_ in list_:
    name,ext = os.path.splitext(file_)
    #Stores the extension type
    ext = ext[1:]
   
    
    #If it is directory, it forces the next iteration

    if os.path.exists(path+'/'+ext):
       shutil.move(path+'/'+file_,path+'/'+ext+'/'+file_)
    #If the directory does not exist, it creates a new directory
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file_,path+'/'+ext+'/'+file_)
