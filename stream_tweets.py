import twitter
import requests as re
import os
import json


# **Task:** Load the values of access tokens and keys from environmental variables to python variables


consumer_key = os.environ['Twitter_Consumer_Key']
consumer_secret = os.environ['Twitter_Consumer_Secret_Key']
access_token = os.environ['Twitter_Access_Token']
access_token_secret = os.environ['Twitter_Access_Secret_Token']


api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)


# Checking the type of api object
print(type(api))


## FOLLOWING FUNCTION WILL COLLECT REAL-TIME TWEETS IN OUR COMPUTER

# data returned will be for any tweet mentioning strings in the list FILTER
FILTER = ['#datascience']

# Languages to filter tweets by is a list. This will be joined by Twitter
# to return data mentioning tweets only in the english language.
LANGUAGES = ['en']


def main(storage_file, fil, lan):
    with open(storage_file, 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(track=fil, languages=lan):
            f.write(json.dumps(line))
            f.write('\n')


# Execute function
main('output.txt', FILTER, LANGUAGES)

