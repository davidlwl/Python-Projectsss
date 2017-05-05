import requests, os, bs4
import time

url = 'http://readcomiconline.to/Comic/Wolverines/Issue-19?id=48340'              # starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd
while not url.endswith('#'):
    print('Downloading page %s...' % url)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
        # Find the URL of the comic image.
    comicElem = soup.select('#divImage img')
    if comicElem == False:
        print('Could not find comic image.')
    else:
         try:
             comicUrl = comicElem[0].get('src')
             # Download the image.
             print('Downloading image %s...' % (comicUrl))
             time.sleep(5)
             res = requests.get(comicUrl)
             res.raise_for_status()
         except requests.exceptions.MissingSchema:
             # skip this comic
             prevLink = soup.select('a[rel="prev"]')[0]
             url = 'http://xkcd.com' + prevLink.get('href')
             continue
            
   
 

