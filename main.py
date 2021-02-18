# Importing Necessary Libraries
import tweepy
import database
import time


# Setting Up Few Properties
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""
TAGS = [
    "#100DaysOfCode", "#CodeNewbie", "#Python", "#EddieHub", "#DEVCommunity",
    "#Quote"
]
ITEMS = 200
SLEEP_PER_ITEM = 5
SLEEP_PER_ROUND = 5 * 60
DELETE_AFTER_COUNT = 10


# Accessing the API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


# Main Function
def run_bot():
    parent = list()
    mentions = api.mentions_timeline()
    search = []
    for tag in TAGS:
        for tweet in tweepy.Cursor(api.search, tag).items(ITEMS):
            if not (tweet in search):
                search.append(tweet)

    parent.extend(mentions)
    parent.extend(search)

    for tweet in parent:
        if not (str(tweet.id) in database.read_info()):
            api.create_favourite(tweet.id)
            api.retweet(tweet.id)
            if "tweepy.models.Status" in type(tweet):
                api.update_status("""
                Thanks for mentioning me. 
                Your tweet has been liked and replied. Please folow my creator @AhammadShawki8 💙      
                """, tweet.id)
            database.write_item(tweet.id)
            time.sleep(SLEEP_PER_ITEM)


# Running the program
if __name__ == "__main__":
    counter = 0
    while True:
        run_bot()
        time.sleep(SLEEP_PER_ROUND)
        if counter == DELETE_AFTER_COUNT:
            database.clear_info()
            counter = 0
        counter += 1