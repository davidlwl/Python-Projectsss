import sys
from collections import Counter
import re
import operator
import pickle
'''
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd) #change emoticons
       
count_all = Counter()
t_only = pickle.load( open( "d.p", "rb" ))
d_only = pickle.load( open( "d.p", "rb" ) )
g_only = pickle.load( open( "g.p", "rb" ) )
count_all.update(terms_only)

print(count_all.most_common(30))

terms_only = [term for term in preprocess(" ".join(d))\
                      if term not in stop and\
                      not term.startswith(('#', '@'))]
d_only = [term for term in preprocess(" ".join(d))\
                      if term not in stop and\
                      not term.startswith(('#', '@'))]
g_only = [term for term in preprocess(" ".join(g))\
                      if term not in stop and\
                      not term.startswith(('#', '@'))]'''

from textblob import TextBlob
def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(tweet)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
    
while True:
    tweet = input('please input phrase/word \n>')
    print(get_tweet_sentiment(tweet))
    print('-'*60)
    
    
        
