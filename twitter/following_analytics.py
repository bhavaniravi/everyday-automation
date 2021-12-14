import tweepy
from dotenv import load_dotenv
import os
import logging
import time
import pandas as pd

load_dotenv()


CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

user_name = "@BhavaniRavi_"

def get_friends_list(user_name):
    return [analyse_user(friend) for friend in tweepy.Cursor(api.friends, screen_name=user_name, count=200).items()]

def unfollow_by_name(user_name):
    api.destroy_friendship(user_name)

def analyse_user(user):
        return (user.screen_name,
        user.followers_count,
        user.friends_count,
        user.favourites_count,
        user.statuses_count,
        user.listed_count,
        user.created_at,
        user.description,
        user.verified)

def construct_dataframe(users):
    print (f"Processing ===> {len(users)}")
    df = pd.DataFrame(users, columns=["user_name", "followers_count", "friends_count", "favourites_count", "statuses_count", "listed_count", "created_at", "description", "is_verified"])
    df.to_csv("twitter/following_analytics.csv", index=False)
    time.sleep(10)

# users = get_friends_list(user_name)
# construct_dataframe(users)

def read_following_list(function):
    def read_csv():
        df = pd.read_csv("twitter/following_analytics.csv")
        return function(df)
    return read_csv

@read_following_list
def find_least_following(df):
    # followers greater than 100 less than 500
    df = df[(df["followers_count"] > 500) & (df["statuses_count"] > 500) & (df["listed_count"] > 10)]
    df = df[df['description'].str.contains("python", na=False, case=False)]
    print (len(df))
    print (df.head(10))
    return df["user_name"].tolist()
    # [unfollow_by_name(user_name) for user_name in df["user_name"]]


def get_all_verified_accounts(df):
    return df[df["is_verified"] == True]



"""
1. Delete following less than 500 followers - 200+ 
2. Delete accounts with less than 500 tweets - 51
"""

def get_twitter_list(list_name):
    return api.list_timeline(list_name)

def create_twitter_list(list_name):
    # if twitter list empty 
    if len(get_twitter_list(list_name)) == 0:
        api.create_list(list_name)

def add_to_twitter_list(list_id, users):
    for user in users:
        api.add_list_members(list_id=list_id, screen_name=user)


add_to_twitter_list("1048532125820104704", find_least_following())



1. Get all the people I follow (Done)
2. Get their bio (Done)
3. Have a list of keywords = ["python", "devops", "writing", "marketing", "indie hacker"]
4. Group people by the above keywords