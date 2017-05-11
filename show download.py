import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
#Getting search results

asking = int(input('Do you need suggestions? Yes - 1, No - 2\n>'))

def search(d):
    mortv = int(input('Are you watching a tv show(1) or movie(2)?'))
    url = 'https://fmovies.is/search?keyword=' + d
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text,'lxml')
    anime = soup.select('.name')
    j = 0
    animes = []
    for i in range(len(anime)):
        f = anime[i].get('href')
        animes.append('https://fmovies.is' + f)
        print (str(j+1)+'. '+anime[i].text.replace('\n',''))
        j += 1

    #Selecting the movie to download
    user_input = int(input('Enter the anime no. to download: '))
    anime_url = animes[user_input-1]
    sc = requests.get(anime_url)
    soup = BeautifulSoup(sc.text,'lxml')
    su = soup.select('.episodes a')
    url = 'https://fmovies.is' + su[0].get('href')

def suggestions():
    print('-' * 60)
    print("Showing you IMDB's top 250 movies!")
    print('-' * 60)
    url = "http://www.imdb.com/search/title?groups=top_250&sort=user_rating&my_ratings=exclude"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    title=soup.select('.lister-item-header a')
    desc=soup.find_all('p', class_='text-muted')
    link = []
    titles = []
#display which movie title
    for y in range(len(desc)):
        link.append(" ".join(desc[y].text.split('\n')))
    for i in range(len(title)):
        print('-' * 60)
        print (str(i+1)+'. '+title[i].text)
        titles.append(title[i].text)
        print('-' * 60)
        print(" ".join(link[i:i+2]))

    number = int(input('which movie would you want to watch?'))
    searcher = titles[number - 1]
    search(searcher)

if asking == 1:
    suggestions()
    
    
searcher = input('Enter movie/tv show name: ')
search(searcher)

if mortv == 2:
    download_now(url)
elif mortv == 1:
    get_shows(url)


def download_now(url):
    browser = webdriver.Chrome(r'C:\Users\Davidlwl\Desktop\chromedriver.exe')
    browser.get(url)
    browser.find_element_by_id('player').click()
    time.sleep(5)
    elem = browser.find_element_by_xpath("(//div[@class='item mbtn download movie pull-right'])")
    elem.click()
    time.sleep(10000000)
    

def get_shows(url):
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text,'lxml')
    anime = soup.select('.active a')
    j = 0
    dsa = []
    for i in range(len(anime)):
        f = anime[i].get('href')
        dsa.append('https://fmovies.is'+
                   f)
        print (str(j+1)+'. '+anime[i].text.replace('\n',''))
        j += 1
    print(dsa)

    user_input = int(input('Enter from which ep no. to start download from: '))
    download_now(dsa[user_input-1])
        
    

    

