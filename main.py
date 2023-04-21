from flask import Flask, render_template

app = Flask("ChanScrapper")


@app.route("/")
def home():
    return render_template("index.html", name="changeon", title="ChanScrapper")


@app.route("/hello")
def hello():
    return "Hello World!"


app.run(host="0.0.0.0", port=3001)
