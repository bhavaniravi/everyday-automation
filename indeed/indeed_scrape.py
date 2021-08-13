# import module
import requests
from bs4 import BeautifulSoup 
import time
import csv
import re
# user define function
# Scrape the data
# and get in string
def getdata(url):
    r = requests.get(url)
    return r.text

import time
  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Fire in the hole!!')
  
# Get Html code using parse
def html_code(url):
  
    # pass the url
    # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
  
    # return html code
    return(soup)
  
# filter job data using
# find_all function
def job_data(soup):
    
    # find the Html tag
    # with find()
    # and convert into string
    job_container = soup.find('div', {"id": "mosaic-provider-jobcards"})
    
    data = []
    for tr in job_container.find_all("a",{"id": re.compile("^job_"), "class": "tapItem"}):
        title_obj = tr.find("h2", {"class":"jobTitle"})
        job_id = tr.get("id")
        company_obj = tr.find("span", {"class":"companyName"})
        location_obj = tr.find("div", {"class":"companyLocation"})
        salary_obj = tr.find("span", {"class":"salary-snippet"})
        yield {"id": job_id,
              "title": title_obj.get_text() if title_obj else None, 
              "company": company_obj.get_text() if company_obj else None, 
              "location": location_obj.get_text() if location_obj else None, 
              "salary": salary_obj.get_text() if salary_obj else None,
              "is_salary": True if salary_obj else False}
  
# filter company_data using
# find_all function
  
  
def company_data(soup):
  
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
    result = ""
    for item in soup.find_all("div", class_="sjcl"):
        data_str = data_str + item.get_text()
    result_1 = data_str.split("\n")
  
    res = []
    for i in range(1, len(result_1)):
        if len(result_1[i]) > 1:
            res.append(result_1[i])
    return(res)
  
  
# driver nodes/main function
if __name__ == "__main__":
    indeed_url = "https://indeed.com/jobs?q="
    # Data for URL
    job = "python junior"
    location = ""
    start = None
    job_data_list = []
    for i in range(1, 200, 10):
        print (i)
        url =   indeed_url+job
        if i != 0:
            url = indeed_url+job+"&start="+str(i)
        soup = html_code(url)
        job_res = list(job_data(soup))
        header = job_res[0].keys()
        with open('indeed_job_us.csv', 'a', encoding='utf8', newline='\n') as output_file:
            fc = csv.DictWriter(output_file, fieldnames=header)
            fc.writeheader()
            fc.writerows(job_res)
        print (len(job_res))
        countdown(10)