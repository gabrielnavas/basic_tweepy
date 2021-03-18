from api import get_api

api = get_api()
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)