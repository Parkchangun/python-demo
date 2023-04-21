from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs

keyword = input("검색어를 입력하세요: ")

wwr_jobs = extract_wwr_jobs(keyword)
indeed_jobs = extract_indeed_jobs(keyword)

total_jobs = wwr_jobs + indeed_jobs

file = open(f"{keyword}.csv", "w", encoding="utf-8")

file.write("Position,Company,Location,URL\n")

for job in total_jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()
