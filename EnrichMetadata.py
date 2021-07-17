
from rauth import OAuth1Service
import json
from ParseJSON import ToObject
import time
# Change these
CONSUMER_KEY = 'VRWc8wizfgRCU1Oyz10fqBpG3'
CONSUMER_SECRET = 'mnUB5Hf7IeQeLi1KcoLHqWKqeDmJ9NkuzrOVxAITJY8kXr4EWt'
ACCESS_TOKEN = '247600111-YFF1DMFAocTMYrm0NEmMGEwi0oQ5IfaXniA5DG6d'
ACCESS_TOKEN_SECRET = 'Ok6282uovenD6qfjH3zBR1trpdUvQZxQBHxN6opy7Q0Ey'

# Instantiate a client
twitter_client = OAuth1Service(name='twitter',
                              consumer_key=CONSUMER_KEY,
                              consumer_secret=CONSUMER_SECRET,
                              base_url='https://api.twitter.com/1.1/')
twitter_session = twitter_client.get_session((ACCESS_TOKEN, ACCESS_TOKEN_SECRET))


def get_metadata(id:str):
    # Request the metadata of two tweets
    while True:
        try:
            IDs = [id]
            URL = 'https://api.twitter.com/1.1/statuses/lookup.json'
            r = twitter_session.get(URL,
                                    params={'id': ','.join(IDs)})
            if len(list(r.json())) <= 0:
                return None
            else:
                if r.json()[0]["geo"] is not None:
                    return r.json()[0]["geo"]["coordinates"]
                else:
                    return None
        except Exception as e:
            print(e)
            time.sleep(60*15)
        except StopIteration:
            break

#get_metadata('263422851133079552')

