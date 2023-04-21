from flask import Flask, render_template
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask("ChanScrapper")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    return render_template("search.html")


app.run(host="0.0.0.0", port=3001)
