#!/usr/bin/env python
# coding: utf-8

# In[1]:


import twitter
import requests as re
import os
import json
# ADD OTHER PACKAGES WE WILL NEED
# <HERE>


# **Task:** Load the values of access tokens and keys from environmental variables to python variables

# In[3]:


consumer_key = os.environ['Twitter_Consumer_Key']
consumer_secret = os.environ['Twitter_Consumer_Secret_Key']
access_token = os.environ['Twitter_Access_Token']
access_token_secret = os.environ['Twitter_Access_Secret_Token']


# In[4]:


api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)


# In[5]:


# Checking the type of api object
print(type(api))


# In[10]:


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


# In[11]:


# Execute function
main('output.txt', FILTER, LANGUAGES)


# **Task:** Edit function `main` so it can store tweets anywhere (location specified as parameter). The FILTER and LANGUAGES should be parameters as well. Test it with different values and languages.

# **Task:** Create File `stream_tweets.py` that can be executed from the Terminal

# **Task:** Start storing tweets with either happy smiley (`:)`) or sad smiley (`:(`). We will use this dataset during the NLP section.

# In[ ]:




