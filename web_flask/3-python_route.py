#!/usr/bin/python3

""" a script that starts a Flask web application
- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
--- /: display “Hello HBNB!”
--- /hbnb: display “HBNB”
---use the option strict_slashes=False in your route definition
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """returns hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    """Return HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """display “C ” followed by the value of the text variable"""
    underscore_str = text.replace("_", " ")
    return f"C {escape(underscore_str)}"


@app.route("/python", strict_slashes=False)
def python_text(text="is cool"):
    return f"Python {escape(text)}"


@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """display “Python”, followed by the value of the text variable"""
    underscore_str = text.replace("_", " ")
    return f"Python {escape(underscore_str)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
