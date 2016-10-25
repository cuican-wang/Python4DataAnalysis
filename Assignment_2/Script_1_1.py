#Import the necessary methods from tweepy library
import os
import http.client
import tweepy
import requests
import urllib.request
import json



#Variables that contains the user credentials to access Twitter API, replace the token&key with yours
access_token = "570787998-19TdCbxP2ES2IMqszhBhylnbuqqYdrwuCTXvdXp4"
access_token_secret = "jchylHmi980oWVjPumMo5Dp20oR8vF522hnGnKqquOVap"
consumer_key = "WC3zaJa2gSa8A8UkFRCn9YWvO"
consumer_secret = "3So1Ld1muwpE2Pwt8nShw0iQL6jialgiNCtnxiiCaH5tHh4ESi"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
print(type(api))


# term = "%23superbowl&result_type=recent"
# res = json.load(urllib.request.urlretrieve("https://api.twitter.com/1.1/search/tweets.json?q="+term))
# res

# threads = []
#
# if __name__ == '__main__':
#     #This handles Twitter authetification and the connection to Twitter Streaming API
#     tweets_num = input("How many tweets do you want to download?(Input numbers):")
#     data_dir = input("Where do you what to store the data?(Input dir like './'):")
#     data_dir = data_dir.strip()
#     data_dir = data_dir.rstrip()
#     os.makedirs(data_dir)
#     os.makedirs(data_dir)
#
#     l = tweepy.StreamListener(api, tweets_num, data_dir)
#     stream = tweepy.Stream(auth, l)
#     print("Connecting to twitter, download in process, please wait...")
#
#     try:
#         stream.sample()
#     except:
#         #print "Error!"
#         stream.disconnect()