# Usecase 
# For my bootcamp I want to give access to my bootcamp users to Github repo. 
# Instead of adding one by one on the UI, I will use this script to add them.

# Create a file `github_ids.txt` with username in each line

from github import Github
from dotenv import load_dotenv
import os

load_dotenv() 
# Create a github personal access token with repos permission
token = os.environ["GITHUB_TOKEN"]


def get_github_id():
    with open("../data/github_ids.txt") as f:
        return list(f)


def add_collaborators(account,repository, permission="push"):
    repo_name = f'{account}/{repository}'
    print (repo_name)
    g = Github(login_or_token=token)
    repo = g.get_repo(repo_name)
    for user in get_github_id():
        user = user.lower().strip()
        print (user)
        repo.add_to_collaborators(user, permission=permission)



account_name = "thelearningdev"
repository = input("Add repo name :: the account is learningdev")
add_collaborators(account_name, repository)

