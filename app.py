from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


import tweepy

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)



screen_name = "macroalf"

statuses = api.user_timeline(screen_name)


print(str(len(statuses)) + " number of statuses have been fetched.")



