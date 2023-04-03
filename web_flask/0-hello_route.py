#!/usr/bin/python3
from flask import Flask
"""
Script that starts a Flask
Web app
"""

app = Flask(__name__)
@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "<p>Hello HBNB!<p>"
app.run(host="0.0.0.0")