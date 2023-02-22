from requests import get
from bs4 import BeautifulSoup

def extract_remoteok_jobs(term):

  url = f"https://remoteok.com/remote-{term}-jobs"
  response = get(url,headers={"User-Agent": "Chrome"})
  
  if response.status_code != 200:
    print("Can't request website")
  else:
    
    soup = BeautifulSoup(response.text, "html.parser")
    sections = soup.find_all('td',class_="company_and_position")
    tags = soup.find_all('td', class_="tags")
  
    jobs=[]
    idx = 0
    for i in sections:
      idx+=1
      job_info = {}
      job_info['idx'] = idx
      job_info['title'] = list(i.find_all("h2"))[0].string.strip()
      job_info['company'] = list(i.find_all("h3"))[0].string.strip()
      locations = i.find_all("div", class_="location")
      more_info=[]
      for j in locations:
         more_info.append(j.string)
      job_info['more_info'] = more_info
      jobs.append(job_info)
  
    idx = 0
    for i in tags:
      idx+=1
      job_info = {}
      tag_dict=[]
      
      tag = i.find_all("h3")
      for j in tag:
        tag_dict.append(j.string.strip())
      job_info['tags'] = tag_dict  
      jobs[idx-1].update(job_info)
    
    return jobs

    for k in jobs:
      print('\n\n')
      for key_, values_ in k.items():
        if values_ == []:
          values_ = "X"
        print(key_,"==>", values_)
