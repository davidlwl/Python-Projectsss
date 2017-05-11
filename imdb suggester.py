import requests
from bs4 import BeautifulSoup
#input a while true here
print('-' * 60)
print("Showing you IMDB's top 250 movies!")
print('-' * 60)
#fix how to input more than 1 word
url = "http://www.imdb.com/search/title?groups=top_250&sort=user_rating&my_ratings=exclude"
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
title=soup.select('.lister-item-header a')
desc=soup.find_all('p', class_='text-muted')
link = []
#display which movie title

for y in range(len(desc)):
    link.append(" ".join(desc[y].text.split('\n')))
for i in range(len(title)):
    print('-' * 60)
    print (str(i+1)+'. '+title[i].text)
    print('-' * 60)
    print(" ".join(link[i:i+2]))
    








    
    

    

