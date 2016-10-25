#!/usr/bin/env python
import twitter


#Setting up Twitter API
CONSUMER_KEY='WC3zaJa2gSa8A8UkFRCn9YWvO'
CONSUMER_SECRET='3So1Ld1muwpE2Pwt8nShw0iQL6jialgiNCtnxiiCaH5tHh4ESi'
ACCESS_TOKEN='570787998-19TdCbxP2ES2IMqszhBhylnbuqqYdrwuCTXvdXp4'
ACCESS_SECRET='jchylHmi980oWVjPumMo5Dp20oR8vF522hnGnKqquOVap'

oauth = twitter.OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=oauth)
term = input("Hi there! What do you want to search?")
res = twitter_api.search.tweets(q=term)
print (res)

