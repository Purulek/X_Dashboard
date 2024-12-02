import tweepy
import pandas as pd

key = 'nTlzKclTzEu56wnYZnq6Ijzcv'

secret_key = 'N3XCBQXQzlilzeTn2LeTma34SgvdC9K54WlIErrdqIkdetaPif'

Bearer_Token = 'AAAAAAAAAAAAAAAAAAAAAIbLxAEAAAAAMqix%2BpC%2BULsYtuctm%2F8gdpquj18%3DdtSFlClrLSMoHKr3ZVtdcfUKp8ku22S7DT6Q3pgqU5V1sa1svI'

acess_token = '1861526408008474626-oZMfhfAFrXN1AlvVCnl0ToT013dvFZ'

secert_token = 'idHyhURsZUUOJY6C1LNgKGOr78VetYcpz0qukCapLpqtb'


client = tweepy.Client(bearer_token=Bearer_Token)

def configure_api(api_key, api_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

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
    return pd.DataFrame(data)





test2 = fetch_tweets(query='#AI')
print(test2)