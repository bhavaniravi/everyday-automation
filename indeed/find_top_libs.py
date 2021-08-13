import csv
from bs4 import BeautifulSoup
import requests
import nltk
import pandas as pd
from tqdm import tqdm
import time

nltk.download('punkt')
nltk.download('stopwords')

headers = {

    'Referer': 'http://google.com',
    'User-Agent': 'Mozilla/5.0'
}

def get_tech_jargon(input_lines):
    "Return a list of tech jargon found in the sentence"
    # function to test if something is a noun
    is_noun = lambda pos: 'NN' in pos[:2] 
    # Break the entence down to words
    tokenized = nltk.word_tokenize(input_lines)  
    return [token.lower() for token in tokenized if token.lower() in get_lib_names()]

def read_from_csv(file_name, columns=None):
    return pd.read_csv(file_name, usecols=columns).to_dict(orient='records')

def get_lib_names():
    return set([val["text"].lower() for val in read_from_csv("python_libraries.csv", columns=["text"])])


def get_job_description(job_id, usa=False):
    job_id = job_id.split("_")[1]
    if usa:
        url=f"https://www.indeed.com/viewjob?jk={job_id}"
    else:
        url=f"https://in.indeed.com/viewjob?jk={job_id}"

    soup = BeautifulSoup(requests.get(url, headers = headers).text, "html.parser")
    description = soup.find("div", {"id": "jobDescriptionText"}).text
    return description



def intersection(description, libraries):
    return set(description).intersection(libraries)


final = []

python_libraries = get_lib_names()
for file_name, is_usa in [("indeed_job_ind.csv", False), ("indeed_job_us.csv", True)]:
    job_list = read_from_csv(file_name, columns=["id"])
    for job in tqdm(job_list):
        try:
            description = get_job_description(job["id"], is_usa)
            tech_jargon = get_tech_jargon(description)
            with open("python_lib_repeated", "a") as f:
                f.write("\n".join(set(tech_jargon)))
            time.sleep(10)
        except Exception as e:
            print (e)