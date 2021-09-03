def all_links():
    pass

def all_accounts():
    pass

def all_tweets():
    pass

def create_list(accounts):
    pass


tweet_link = input("Add tweet to scrape ::")
option = input("""What should I scrape?
1. All links
2. All accounts
3. All tweets""")

if option == 1:
    links = get_links()
elif option == 2:
    accounts = get_accounts()
    create_list = input("Do you wanna create list [y/n]?")
    if choice == "y":
        create_list()
elif option == 3:
    all_tweets()