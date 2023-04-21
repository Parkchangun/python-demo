from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from file import save_to_file

keyword = input("검색어를 입력하세요: ")

wwr_jobs = extract_wwr_jobs(keyword)
indeed_jobs = extract_indeed_jobs(keyword)
jobs = wwr_jobs + indeed_jobs

save_to_file(keyword, jobs)
