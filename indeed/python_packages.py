import markdown
from bs4 import BeautifulSoup
import requests
import pandas as pd

body_markdown = requests.get("https://raw.githubusercontent.com/vinta/awesome-python/master/README.md").text
body_markdown = markdown.markdown(body_markdown)

soup = BeautifulSoup(body_markdown, "html.parser")
data = [{"text": link.text, "link":link.get('href')} for link in soup.find_all('a') if link.text != "" and "http" in link.get("href")]
pd.DataFrame(data).to_csv("python_libraries.csv", index=False)