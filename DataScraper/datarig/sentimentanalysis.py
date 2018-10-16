import tweepy
from textblob import TextBlob

def percentage(part):
    return 100 * float(part)/200


def get_sentiments(keyword, api):
    tweets = tweepy.Cursor(api.search, q=keyword).items(200)
    
    positive = 0
    negative = 0
    neutral =  0
    polarity = 0

    n = len([x for x in tweets if TextBlob(x.text).sentiment.polarity==0])
    neg = len([x for x in tweets if TextBlob(x.text).sentiment.polarity < 0])
    p =len([x for x in tweets if TextBlob(x.text).sentiment.polarity > 0])
    
    p = round(percentage(p), 2)
    neg = round(percentage(neg), 2)
    n = round(percentage(n), 2)
    
    return [p, n, neg]


    

        
        
            





