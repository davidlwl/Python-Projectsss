from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    #note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
    #from vaderSentiment import SentimentIntensityAnalyzer

# --- examples -------

while True:
    sentences = input('please input your sentence! \n>')
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(sentences)
    print("{:-<65} {}".format(sentences, str(vs)))
