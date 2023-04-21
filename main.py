from flask import Flask, render_template, request, redirect
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask("ChanScrapper")

db = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    if keyword == None:
        return redirect("/")

    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run(host="0.0.0.0", port=3001)
