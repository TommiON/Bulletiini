from flask import render_template
from application import app
from application.threads.models import Thread

@app.route("/")
def index():
    return render_template("threadsList.html", threads=Thread.query.all())
    # return render_template("index.html")
