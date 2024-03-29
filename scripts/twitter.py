#!/usr/bin/env python

import time
import os
from sys import exit

try:
    from tweepy import Stream, OAuthHandler
    from tweepy.streaming import StreamListener
except ImportError:
    exit('This script requires the tweepy module\nInstall with: sudo pip install tweepy')

import blinkt


ckey = os.environ['TWITTER_CONSUMER_KEY']     # Consumer key
csecret = os.environ['TWITTER_CONSUMER_SECRET']  # Consumer secret
atoken = os.environ['TWITTER_ACCESS_KEY']   # Access token
asecret = os.environ['TWITTER_ACCESS_SECRET']  # Access secret


class listener(StreamListener):
    def on_data(self, data):
        blink_blinkt()
        return True

    def on_error(self, status):
        print(status)


def blink_blinkt():
    for i in range(3):
        for j in range(blinkt.NUM_PIXELS):
            blinkt.set_pixel(j, 255, 0, 0)

        blinkt.show()
        time.sleep(0.1)

        for j in range(blinkt.NUM_PIXELS):
            blinkt.set_pixel(j, 0, 0, 0)

        blinkt.show()
        time.sleep(0.2)


def twitter():
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterstream = Stream(auth, listener())
    twitterstream.filter(track=['#michaelbolton'])