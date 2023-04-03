#!/usr/bin/python3
"""
Script that starts a Flask
Web app
"""
from flask import Flask

app = Flask(__name__)
app.run("0.0.0.0")
@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "<p>Hello HBNB!<p>"