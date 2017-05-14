
import requests
from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import webbrowser


def summarize(input_file, output_num):
    #take out specific stop words
    stop_words = set(stopwords.words('english'))
    #split input text into sentences
    input_text = sent_tokenize(input_file)
    #getting freq of each word into a dict  
    word_values = {}

    for sentence in input_text:
        words = sentence.split(' ')
        for word in words:
            word = strip(word)
            if not word in stop_words:
                if not word in word_values:
                    word_values[word] = 1
                else:
                    word_values[word] += 1

    sentence_values = []
    for sentence in input_text:
        sentence_value = 0   
        words = sentence.split(' ')
        for word in words:
        #counts the sentence value using word_values dictionary

            
            sentence_value += word_values.setdefault(word, 0)
        sentence_values.append(sentence_value)
        

    #how many sentences do you want = output_num
    for ii in range(0, output_num):
        highest_val_ind = sentence_values.index(max(sentence_values))
        print(input_text[highest_val_ind])
                    
        del input_text[highest_val_ind]
        del sentence_values[highest_val_ind]

def strip(word):
    return word.strip().strip(',').strip(':').strip('(').strip(')').lower()


def get_only_text(url):

    page = urllib.request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page, 'lxml')
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return soup.title.text, text


feed_xml = urllib.request.urlopen('http://www.straitstimes.com/print/top-of-the-news/rss.xml').read()
feed = BeautifulSoup(feed_xml.decode('utf8'), 'lxml')
to_summarize = list(map(lambda p: p.text, feed.find_all('guid')))

for article_url in to_summarize[:10]:
    i = to_summarize[:10].index(article_url)
    title, text = get_only_text(article_url)
    print('-' * 80)  
    print (str(i+1) + ". " + title[:-20])
    print('-' * 80)  
    if summarize(text, 2) == None:
        pass
    else:
        for s in summarize(text, 2):
            print (s)
    

while True:
    news_list = []
    raw = input('Which articles would you like to read?')
    for i in raw.replace(',', ''):
        news_list.append(i)
    for x in news_list:
        webbrowser.open_new_tab(to_summarize[int(x)-1])
    

    

            

    






    
