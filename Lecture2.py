import flask
import os
import random
import tweepy
import json
import requests
#git push heroku master
app = flask.Flask(__name__)
accessToken =  "1424806820-kMUoLxUIubxJJ8gXwsVNrPUSaoXtQ0gXzOSTbyZ"
accessTokSec = "LxQV4pl0kB3olfxWRb9nrtSmtGjLkf1tPhE2gJhuOzB7d"
consumer_token = "Dg8muOuQWuqjdlyPEmvyDBhpO"
consumer_secret = "7VmV5URL9vSX2fMZHLDpHIH8boRI9wt6UP3WBolGW1EdxmvNGg"
max_tweets = 100
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(accessToken, accessTokSec)
api = tweepy.API(auth)  
query = ['anime%20quotes', 'ramen', 'the%20Struggle', 'college'] #terms to query twitter
getty_api_key = "ng993nc5jzchjde38sa4fztc"
count = 0
tweets = []
for term in query:
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=term, lang="en").items(max_tweets)]
    for tweet in searched_tweets:
        if (not tweet.retweeted) and (tweet not in tweets) and ('RT @' not in tweet.text) and ('media' not in tweet.entities): 
        #'https:' not in tweet.text:
            tweets.append(tweet.text)
            
            
url_test = 'https://api.gettyimages.com/v3/search/images?fields=id,title,thumb,referral_destinations&sort_order=best&phrase=ramen'
headers = {'Api-Key' : getty_api_key}
res = requests.get(url_test, headers=headers, )
data  = res.json()
#gets all IDs from json, caps at 20
count = 0
gettyList = []

for element in data['images']:
    gettyList.append(element['id'])
    print element['id']

for ids in gettyList:
   gettyImg =  gettyList[random.randrange(0, len(gettyList))]
   return flask.render_template("index.html", gettyImg = gettyImg)
