tags = ["write", "tech", "book", "devops", "machine learning", "startups", "business"]

# Fetch the tweet and timestamp

def fetch_tweet(tweet_link):
    pass

# Writing, tech, books, devops, startups are some of the categories I know
def tag_tweet(tweet):
    pass


file_path = "../data/bookmark_tweets.csv"
tweet_df = pd.read_csv(file_path)

for tweet_link in tweet_df["Name"]:
    tweet = fetch_tweet(tweet_link)