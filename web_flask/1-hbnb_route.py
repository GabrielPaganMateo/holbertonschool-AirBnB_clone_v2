#!/usr/bin/python3
"""This is the module documentation"""
from web_flask.__init__ import app
"""
Script that starts a Flask
Web app for my HBNB clone project
"""

@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)