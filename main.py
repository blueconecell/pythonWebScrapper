from extractors.remoteok import extract_remoteok_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file
keyword = input("What do you want to search for? ")

a = extract_remoteok_jobs(keyword)
b = extract_wwr_jobs(keyword)
c = a+b

for j in c:
    print(j['href'])

# jobs = []
# jobs.append(extract_wwr_jobs(keyword))
# jobs.append(extract_remoteok_jobs(keyword))
# save_to_file(keyword, jobs)