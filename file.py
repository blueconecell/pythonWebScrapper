def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w", encoding='utf-8')
    file.write("title, company, region, url\n")
    for sites in jobs:
        for job in sites:
            file.write(f"{job['title']}, {job['company']},{job['region']},{job['href']}\n")
    file.close()