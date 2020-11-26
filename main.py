import tweepy
from os import environ
from datetime import datetime

def get_api():

    API_KEY = environ["API_KEY"]
    API_KEY_SECRET = environ["API_KEY_SECRET"]
    CON_KEY = environ["CON_KEY"]
    CON_SECRET = environ["CON_SECRET"]
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(CON_KEY, CON_SECRET)
    # Create API object
    api = tweepy.API(auth)
    return api

print(datetime.now())
api = get_api()

# Create a tweet
# api.update_status("Hello Tweepy")
# print (api.rate_limit_status())

api.update_with_media("V_s.png", status="test")