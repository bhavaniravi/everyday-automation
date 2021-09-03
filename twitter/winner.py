import tweepy
from dotenv import load_dotenv
import os
import logging
import time

load_dotenv()


CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

user_name = "@BhavaniRavi_"

tweet_id = "1430907899648299009"
replies = tweepy.Cursor(api.search, q='to:{}'.format(user_name),
                                since_id=tweet_id).items()

final_set = set()
while True:
    try:

        reply = replies.next()
        if not hasattr(reply, 'in_reply_to_status_id_str'):
            print (reply.author.screen_name)
            continue
        if str(reply.in_reply_to_status_id) == tweet_id:
            final_set.add(reply.author.screen_name)

    except tweepy.RateLimitError as e:
        print("Twitter api rate limit reached".format(e))
        time.sleep(60)
        continue

    except tweepy.TweepError as e:
        print("Tweepy error occured:{}".format(e))
        break

    except StopIteration:
        break

    except Exception as e:
        print("Failed while fetching replies {}".format(e))
        break


final_set = list(final_set)

final_set.remove("BhavaniRavi_")
final_set.remove("arvidkahl")

import random
print (f"Getting Names....")
time.sleep(3)
print (f"Total Participants :: {len(final_set)}")
time.sleep(3)

print (f"\n\nParticipants list")
for name in final_set:
    time.sleep(0.5)
    print (name)


time.sleep(2)
print("\n\n  🎊 🎊 And the Winners Are.... 🎊 🎊")

time.sleep(3)
print ("1. " + random.choice(final_set))
time.sleep(2)
print ("2. " + random.choice(final_set))

time.sleep(2)
print ("\n\n🎁 Congratulations !! 🎁")