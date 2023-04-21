from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
    wework_url = "https://weworkremotely.com"
    base_url = f"{wework_url}/remote-jobs/search?term="

    response = get(f"{base_url}{keyword}")

    if response.status_code != 200:
        print("Can`t request websit")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")

        results = []

        for job_section in jobs:
            job_posts = job_section.find_all("li", class_="feature")

            for post in job_posts:
                anchors = post.find_all("a")
                anchor = anchors[1]
                link = anchor["href"]

                company, kind, region = anchor.find_all("span", class_="company")

                title = anchor.find("span", class_="title")

                job_data = {
                    "link": f"{wework_url}{link}",
                    "company": company.string,
                    "location": region.string,
                    "position": title.string,
                }
                results.append(job_data)

        return results
