from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(term):

  url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={term}"
  response = get(url,headers={"User-Agent": "Chrome"})
  
  if response.status_code != 200:
    print("Can't request website")
  else:
    
    soup = BeautifulSoup(response.text, "html.parser")
    sections = soup.find_all('li',class_="feature")
  
    jobs=[]
    idx = 0
    for i in sections:
      idx+=1
      job_info = {}
      job_info['idx'] = idx
      job_info['title'] = list(i.find_all("span",class_="title"))[0].string.strip().replace(","," ")
      job_info['company'] = list(i.find_all("span",class_="company"))[0].string.strip().replace(","," ")
      # if i.find_all("span",class_="date"):
      #   job_info['date'] = list(i.find_all("span",class_="date"))[0].string.strip()
      job_info['region'] = list(i.find_all("span",class_="region company"))[0].string.strip().replace(","," ")
      idx_href = 0
      for href in i.find_all("a",href=True):
        idx_href+=1
        if idx_href%2==0:
          job_info['href'] = "https://weworkremotely.com"+href['href']

      jobs.append(job_info)
    return jobs


# jobs = extract_wwr_jobs("react")
# for k in jobs:
#   print('\n\n')
#   for key_, values_ in k.items():
#     if values_ == []:
#       values_ = "X"
#     print(key_,"==>", values_)