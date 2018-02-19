from flask import render_template, session, url_for, flash, redirect
from . import main

@main.route("/")
def index():
    #session['user_id'] = 1
    
    try:
        user_id = session["user_id"]
    except KeyError:
        redirect(url_for("auth.login"))
    
    return render_template("index.html")