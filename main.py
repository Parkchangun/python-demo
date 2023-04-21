# from extractors.wwr import extract_wwr_jobs

# jobs = extract_wwr_jobs("vue")
# print(jobs)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get(f"https://www.indeed.com/jobs?q=python&limit=10")

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all("li", recursive=False)
results = []

for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        anchor = job.select_one("h2 a")
        title = anchor["aria-label"]
        link = anchor["href"]
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
            "link": f"https://kr.indeed.com{link}",
            "company": company.string,
            "location": location.string,
            "position": title,
        }
        results.append(job_data)

for result in results:
    print(result, "\n////")

while True:
    pass
