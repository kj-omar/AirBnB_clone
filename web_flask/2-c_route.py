#!/usr/bin/python3
""" A flask Application that listens on 0.0.0.0, port 5000 """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello Route"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string"""
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def C_Text(text):
    """Returns a string"""
    return("C {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
