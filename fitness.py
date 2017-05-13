
import requests, os
from bs4 import BeautifulSoup
from random import randint
from os import listdir
from PIL import Image as PImage
import time

path = r'C:\Users\\Desktop\Python Projects\fitness'
def loadImages(path):
    # return array of images
    imagesList = listdir(path)
    loadedImages = []
    image = imagesList[0]
    with PImage.open(path + "/" + image) as f:
        f.show()
    input('done!')
    while True:
        try:
            os.remove(path + "/" + image)
            break
        except:
            time.sleep(1)
    
loadImages(path)

push = input('How many push ups will you be doing today?')
print(randint(20,40))
print('-' * 60)
push = input('How many sit-ups will you be doing today?')
print(randint(20,40))
print('-' * 60)
push = input('How many squats will you be doing today?')
print(randint(20,40))
print('-' * 60)
push = input('How many calf raises will you be doing today?')
print(randint(20,40))
print('-' * 60)
push = input('How many bicep curls will you be doing today?')
print(randint(20,40))


'''
#download the images
url = 'http://amerrylife.com/2014/12/09/50-fitness-motivation-quotes-for-your-motivation-board/'
sc =requests.get(url)
soup = BeautifulSoup(sc.text,'lxml')
os.makedirs('fitness', exist_ok=True)

comicElem = soup.select('p img')
for i in range(len(comicElem)):
    comicUrl = comicElem[i].get('src')
    print('Downloading image %s...' % (comicUrl))
    res = requests.get(comicUrl)
    imageFile = open(os.path.join('fitness', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()'''

