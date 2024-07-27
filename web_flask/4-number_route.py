#!/usr/bin/python3
""" python script that starts a Flask
web application
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<txt>", strict_slashes=False)
def C(txt):
    txt = txt.replace("_", " ")
    return "C {}".format(txt)


@app.route("/python/", defaults={'txt': 'is cool'})
@app.route("/python/<txt>", strict_slashes=False)
def Python(txt):
    txt = txt.replace("_", " ")
    return "Python {}".format(txt)


@app.route("/number/<n>", strict_slashes=False)
def Number(n):
    try:
        n = int(n)
        return "{} is a number".format(n)
    except ValueError:
        pass
        


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
