import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
#Getting search results
search = input('Enter movie/tv show name: ')
mortv = int(input('Are you watching a tv show(1) or movie(2)?'))
url = 'https://fmovies.is/search?keyword=' + search
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

def download_now(url):
    browser = webdriver.Chrome(r'C:\Users\Davidlwl\Desktop\chromedriver.exe')
    browser.get(url)
    browser.find_element_by_id('player').click()
    time.sleep(5)
    elem = browser.find_element_by_xpath("(//div[@class='item mbtn download movie pull-right'])")
    elem.click()



def get_shows(url):
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text,'lxml')
    anime = soup.select('.active a')
    j = 0
    dsa = []
    for i in range(len(anime)):
        f = anime[i].get('href')
        dsa.append(f)
        print (str(j+1)+'. '+anime[i].text.replace('\n',''))
        j += 1
    print(dsa)

    user_input = int(input('Enter from which ep no. to start download from: '))
    download_now(dsa[user_input-1])
        
    
if mortv == 2:
    download_now(url)
elif mortv == 1:
    get_shows(url)
    

