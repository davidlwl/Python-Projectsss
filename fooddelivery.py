import requests
import os,sys
from bs4 import BeautifulSoup
import webbrowser
url = 'http://singpromos.com/bydate/ontoday/?s=food+delivery'
sc =requests.get(url)
soup = BeautifulSoup(sc.text,'lxml')
title = soup.select('.entry-title a')
total = soup.select('.currentTab1 a')
present = int(total[0].text[8:])

for i in range(present):
    print(str(i+1) + ". " + title[i].text.strip())
    print('*' *80)

if present >10:
    url2 = 'http://singpromos.com/bydate/ontoday/page/2/?s=food+delivery'    
    sc2 =requests.get(url2)
    soup2 = BeautifulSoup(sc2.text,'lxml')
    title2 = soup2.select('.entry-title a')   
    for i in range(present - 10):
        print(i+1, title2[i].text.strip())
        print('*' *80)
else:
    pass

qn = input('visit site?')
if qn == 'yes':
    webbrowser.open('http://singpromos.com/bydate/ontoday/?s=food+delivery')
    
    
    
                             
