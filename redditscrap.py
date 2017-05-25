import praw
import requests
from bs4 import BeautifulSoup
import re

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')

#get pics
def downloadImage(imageUrl, localFileName):
    response = requests.get(imageUrl)
    with open(localFileName, 'wb') as fo:
        for chunk in response.iter_content(4096):
            fo.write(chunk)

for index, submission in enumerate(reddit.subreddit('GetMotivated').hot(limit=200)):
    try:
        if submission.url[-3:] in ['jpg', 'png']:
            downloadImage(submission.url, r'C:'+'/'+submission.title+submission.url[-4:])
            print('Downloaded' + submission.url )
    except OSError:
        pass
    
    try:
        if 'imgur' in submission.url:
            downloadImage(submission.url, r'C:'+'/'+submission.title+'.jpg')  
            print('Downloaded' + submission.url )
    except OSError:
        pass 
        


