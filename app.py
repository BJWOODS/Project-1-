import flask
import os
import random
import tweepy
import simplejson as json
import requests

idUniques = []
imgUniques = []



#git push heroku master

count = 0
tweets = dict()
tweetsInfo = []
            
app = flask.Flask(__name__)            
@app.route('/') #python decorator
#gets all IDs from json, caps at 20


def index(gettyImg = None):
    
    accessToken = os.getenv("accessToken")
    accessTokSec = os.getenv("accessTokSec")
    consumer_token = os.getenv("consumer_token")
    consumer_secret = os.getenv("consumer_secret")
    max_tweets = 30
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(accessToken, accessTokSec)
    api = tweepy.API(auth)  
    getty_api_key = os.getenv("getty_api_key")
    
    unique = False #boolean used for checking uniques
    query = ['ramen', 'college','travel','life'] #terms to query twitter
    word = random.choice(query)
    
    
    url_test = 'https://api.gettyimages.com/v3/search/images?fields=id,title,thumb,referral_destinations&sort_order=best&phrase='+word
    headers = {'Api-Key' : getty_api_key}
    gettyList = []
    count = 0
    res = requests.get(url_test, headers=headers)
    j=0
    data  = res.json()
    for term in query:
        searched_tweets = [status for status in tweepy.Cursor(api.search, q=term, lang="en").items(max_tweets)]
        for tweet in searched_tweets:
            if (not tweet.retweeted) and (tweet not in tweets) and ('RT @' not in tweet.text) and ('media' not in tweet.entities): 
            #'https:' not in tweet.text:
                
                tweets[j] = [tweet.text,tweet.id_str,tweet.user.name]
                j+=1
                
               
               # clickPick = tweet.author.profile_image_url_https
                
                
                
    
                           
           
    
                
    for element in data['images']:
        print element['id']
    global count
    count = random.randrange(0, len(tweets))
    tString = tweets[count][0]
    uStringID = tweets[count][1]
    uStringU = tweets[count][2]
  
    #count = count + 1 #Could use for linear iteration through twitter list
    
    for element in data['images']:
        gettyList.append(element['id'])
        print element['id']
    
    for ids in gettyList:
       gettyImg =  gettyList[random.randrange(0, len(gettyList))]
    
    gettyImg = random.choice(gettyList)
      
    print "getty img var: "+gettyImg
        
        
    return flask.render_template("index.html", 
        tString = tString, 
        gettyImg= "http://media.gettyimages.com/photos/-id"+gettyImg,uStringID=uStringID,uStringU = uStringU)
        #user=user,user_id=user_id


    
app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP','0.0.0.0')
    

)
    
    