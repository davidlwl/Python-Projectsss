import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
#Getting search results

asking = int(input('Do you need suggestions? Yes - 1, No - 2\n>'))

def download_now():
    
    
    time.sleep(3)
    browser.find_element_by_id('player').click()
    time.sleep(5)
    elem = browser.find_element_by_xpath("(//div[@class='item mbtn download movie pull-right'])")
    elem.click()
    


def get_subtitles(movie_id):
    urls ='https://www.opensubtitles.org/en/search2/sublanguageid-eng/moviename-' + movie_id
    print(urls)
    sc = requests.get(urls)
    soup = BeautifulSoup(sc.text,'lxml')
    anime = soup.select('.bnone')
    j = 0
    amd = []
    for i in range(len(anime)):
        f = anime[i].get('href')
        amd.append('https://www.opensubtitles.org'+f)
        print (str(j+1)+'. '+anime[i].text.replace('\n',''))
        j += 1
    user_input = int(input('Enter from which subtitle to start download from: '))
    browser = webdriver.Chrome()
    browser.execute_script("window.open('www.google.com', 'new_window')")
    browser.switch_to.window(browser.window_handles[1])
    browser.get(amd[user_input-1])
    #download manually
    

def get_shows(url):
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text,'lxml')
    animea = soup.select('.active a')
    j = 0
    dsa = []
    for i in range(len(animea)):
        f = animea[i].get('href')
        dsa.append('https://fmovies.is'+f)
        print (str(j+1)+'. '+animea[i].text.replace('\n',''))
        j += 1
    print(dsa)

    shopList = [] 
    maxLengthList = 10
    while len(shopList) < maxLengthList:
        users_input = int(input('Enter from which ep no. to start download \nEnter 0 to stop: '))
        shopList.append(users_input)
        print(shopList)

    for x in shopList:
        download_now(dsa[int(x)-1])
       
     
def search(d):
    mortv = int(input('Are you watching a tv show(1) or movie(2)?'))
    url = 'https://fmovies.is/search?keyword=' + d
    browser = webdriver.Chrome()
    browser.get(url)
    browser.refresh()
    moviename = browser.find_element_by_class_name('name')
    moviename.click()
    
    time.sleep(5)
    browser.find_element_by_id('player').click()
    time.sleep(3)
    elem = browser.find_element_by_xpath("(//div[@class='item mbtn download movie pull-right'])")
    elem.click()
    elems = browser.find_element_by_xpath("(//div[@class='item mbtn download subtitle pull-right hidden-xs'])") 
    movie_id = d
    

    if mortv == 2:
        get_subtitles(movie_id)
    elif mortv == 1:
        get_shows(url)
        asker = input('are the downloads ready?')
        if asker == 'yes':        
            get_subtitles()                       
                         

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
        print(" ".join(link[2*i:2*i+2]))
        

    number = int(input('which movie would you want to watch?'))
    searcher = titles[number - 1]
    print(searcher)
    search(searcher)

if asking == 1:
    suggestions()
    
searcher = input('Enter movie/tv show name: ')
search(searcher)


'''
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
    url = 'https://fmovies.is' + su[0].get('href')'''

    

    

