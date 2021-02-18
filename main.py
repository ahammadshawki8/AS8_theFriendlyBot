import tweepy
import database
import time

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""
TAGS = ["#100DaysOfCode", "#CodeNewbie", "#Python", "#EddieHub", "#DEVCommunity", "#Quote"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

parent = list()
mentions = api.mentions_timeline()
home = [x for x in api.home_timeline() if any(TAGS) in x.text]

parent.extend(mentions)
parent.extend(home)

for item in parent:
    pass
