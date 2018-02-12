from flask import render_template, flash
from . import main

@main.route("/")
def index():
    return "Hello"