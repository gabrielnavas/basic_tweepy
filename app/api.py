import tweepy
from tokens import get_tokens 


def get_api(): 
    tokens = get_tokens()
    auth = tweepy.OAuthHandler(tokens['consumer_key'], tokens['consumer_secret'])
    auth.set_access_token(tokens['access_token'], tokens['access_token_secret'])

    api = tweepy.API(auth)
    return api
