from flask import render_template, session, url_for, flash
from . import main

#session['user_id'] = 1

@main.route("/")
def index():
    session['user_id'] = 1
    return render_template("index.html")