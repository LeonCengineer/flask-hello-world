from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


import tweepy

auth = tweepy.OAuth1UserHandler(
   hxlKCgcrMtFweITfuY2PVc0b6, YIoohvFDa1dsgWzl03pDtHyNXycmQZFTGDabiH9PHJTXu0sjDL, 18368941-6MRapL0PCELHw0RagwsyrgQntyoxUy91kjxBAHMQD, RkTOdUgFDvVzowFBgso65nmVoYPMASVFOb5PXCDZ278E
)

api = tweepy.API(auth)


screen_name = "macroalf"

statuses = api.user_timeline(screen_name)


print(str(len(statuses)) + " number of statuses have been fetched.")



