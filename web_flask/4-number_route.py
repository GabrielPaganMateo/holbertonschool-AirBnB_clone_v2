#!/usr/bin/python3
"""This is the module documentation"""
from flask import Flask
"""
Script that starts a Flask
Web app for my HBNB clone project
"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    return "C " + f'{text}'.replace("_", " ")


@app.route("/python/", strict_slashes=False, defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    if text == "is cool":
        return "Python is cool"
    else:
        return "Python " + f'{text}'.replace("_", " ")
    

@app.route("/number/<n>", strict_slashes=False)
def number(n):
    if n is type(int):
        return f'{n} is a number'
    else:
        pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
