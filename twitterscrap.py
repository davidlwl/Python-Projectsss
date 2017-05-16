import sys
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
import json
from tweepy.streaming import StreamListener
import operator
from collections import Counter
 
consumer_key = 
consumer_secret = 
access_token = '
access_secret = ''
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

# collect tweets for a specific hashtag eg. #python 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('trump.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#trump'])

import re

# tokenize words/with emoticons and hashtags from .json file 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd) #change emoticons


#count most used words
from nltk.corpus import stopwords
import string
from nltk import bigrams
from collections import defaultdict

com = defaultdict(lambda : defaultdict(int))
import ast
fname = 'trump.json'
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['RT', 'via', '…', 'Python', '#python', '#Python']
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f: #for every tweet
        if line.strip():
            tweet = json.loads(line.strip())
            # Count terms only (no hashtags, no mentions)
            if 'text' in tweet:
                terms_only = [term for term in preprocess(tweet['text'].translate(non_bmp_map))\
                              if term not in stop and\
                              not term.startswith(('#', '@'))]

                count_all.update(terms_only) 
           
                # Build co-occurrence matrix( number of times the term x has been seen in the same tweet as the term y)
                for i in range(len(terms_only)-1):            
                    for j in range(i+1, len(terms_only)):
                        w1, w2 = sorted([
                            terms_only[i], terms_only[j]])                
                        if w1 != w2:
                            com[w1][w2] += 1
            else:
                pass

    # For each term, look for the most common co-occurrent terms
    com_max = []            
    for t1 in com:
        t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
        for t2, t2_count in t1_max_terms:
            com_max.append(((t1, t2), t2_count))
    # Get the most frequent co-occurrences
    terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
    print(terms_max[:5])
    print(count_all.most_common(10))
    

#visualize data
import vincent
import pandas
import json
fname = 'trump.json'
with open(fname, 'r') as f:
    count_all = Counter()
    dates_trump = []
    # f is the file pointer to the JSON data set
    for line in f: #for every tweet
        if line.strip():
            tweet = json.loads(line)
            # let's focus on hashtags only at the moment
            terms_hash = [term for term in preprocess(tweet['text'].translate(non_bmp_map)) if term.startswith('#')]
            # track when the hashtag is mentioned
            count_all.update(terms_hash)
    
        if '#Trump' in terms_hash:
            dates_trump.append(tweet['created_at'])
     
    # a list of "1" to count the hashtags
    ones = [1]*len(dates_trump)
    # the index of the series, find date format
    idx = pandas.DatetimeIndex(dates_trump)
    # the actual series (at series of 1s for the moment)
    trump = pandas.Series(ones, index=idx)
     
    # Resampling / bucketing
    per_minute = trump.resample('1Min').sum().fillna(0)
    
    time_chart = vincent.Line(trump)
    time_chart.axis_titles(x='Time', y='Freq')
    time_chart.to_json('time_chart.json', html_out=True, html_path='chart.html')



 
        
