# from extractors.wwr import extract_wwr_jobs

# jobs = extract_wwr_jobs("vue")
# print(jobs)

from extractors.indeed import extract_indeed_jobs

jobs = extract_indeed_jobs("python")
print(len(jobs))
