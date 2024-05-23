from flask import Flask, render_template
from requests import get, Response


app = Flask("Frontend")
BACKEND_URL = "http://127.0.0.1:8000"


@app.get("/")
def index():
    context = {
        "result":get(f"{BACKEND_URL}/")
    }
    return render_template("index.html", **context)


@app.get("/quotes")
def quotes_list():
    quotes = []
    i = 0
    url_response = get(f"{BACKEND_URL}/quote/{i}")
    while url_response.status_code == 200:
        i += 1
        quotes.append(url_response.json())
        url_response = get(f"{BACKEND_URL}/quote/{i}")

    context = {
        "result": quotes
    }
    return context
    return render_template("index.html", **context)



