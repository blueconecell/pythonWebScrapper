from requests import get
from bs4 import BeautifulSoup
from extractors.remoteok import extract_remoteok_jobs
from extractors.wwr import extract_wwr_jobs

keyword = "python"
jobs = []
jobs.append(extract_wwr_jobs(keyword))
jobs.append(extract_remoteok_jobs(keyword))
idx = 0
print('#######################')
for l in jobs:
    for k in l:
        print('\n\n')
        idx+=1
        print(idx)
        for key_, values_ in k.items():
            if values_ == []:
                values_ = "X"
            print(key_,"==>", values_)