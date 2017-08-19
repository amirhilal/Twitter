import random
from time import time
from tweepy.auth import OAuthHandler, API
import requests
import os

# Credentials to access Twitter API
ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXXXXXXXXXXX'
CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXX'

# Initiate the connection to Twitter API
Auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
Auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
TwitterBot = API(Auth)

images = ["http://www.image-link.com"]

def tweet_image(url, message):
    api = TwitterBot
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")

tweet_image(random.choice(images), "#SMT @RealDonaldTrump")
