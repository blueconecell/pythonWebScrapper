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
      job_info['title'] = list(i.find_all("span",class_="title"))[0].string.strip()
      job_info['company'] = list(i.find_all("span",class_="company"))[0].string.strip()
      job_info['date'] = list(i.find_all("span",class_="date"))[0].string.strip()
      job_info['region'] = list(i.find_all("span",class_="region company"))[0].string.strip()
      jobs.append(job_info)
    return jobs

