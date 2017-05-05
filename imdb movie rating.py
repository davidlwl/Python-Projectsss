import requests
from bs4 import BeautifulSoup
#input a while true here
print('what movie would you like to watch? Input in this format:\nAll+The+Best')
movie = input('>: ')
#fix how to input more than 1 word
url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + movie+ "&s=all"
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
title=soup.select('.result_text')
link = []
#display which movie title
for i in range(len(title)):
    link.append('http://www.imdb.com' + title[i].find('a')['href'])
for i in range(len(title)):
    print (str(i+1)+'. '+title[i].find('a').text)
#ask for which movie
actual = int(input('which movie/tv show sir?'))
url = link[actual - 1]
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
rating = soup.select('.ratingValue')
description = soup.select('.summary_text')
print(rating[0].text)
print(" ".join(description[0].text.split()))

movie = input('>: ')






    
    

    

