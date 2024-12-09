import tweepy
import pandas as pd

Bearer_Token = ''

client = tweepy.Client(bearer_token=Bearer_Token)



def fetch_tweets(query, max_results=10):
    response = client.search_recent_tweets(query=query, tweet_fields=['created_at', 'public_metrics'], max_results=max_results)
    tweets = response.data
    if not tweets:
        return pd.DataFrame()
    
    data = [{
        "text": tweet.text,
        "created_at": tweet.created_at,
        "retweets": tweet.public_metrics['retweet_count'],
        "likes": tweet.public_metrics['like_count']
    } for tweet in tweets]
    pd.DataFrame(data)
    data.set_index(inplace = True)
    with open ('daata.txt', 'w', 'UTF=8') as File:
        File.write(data)
    




test2 = fetch_tweets(query='#AI')