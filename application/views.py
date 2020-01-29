from flask import redirect, url_for, render_template
from application import app

@app.route("/")
def index():
    return render_template("index.html")
