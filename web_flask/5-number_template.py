#!/usr/bin/python3
""" A flask Application that listens on 0.0.0.0, port 5000 """
from flask import Flask, render_template


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
def c_Text(text):
    """Returns a string"""
    return("C {}".format(text.replace("_", " ")))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text="is cool"):
    """Returns a string"""
    return("Python {}".format(text.replace("_", " ")))


@app.route("/number/<int:n>", strict_slashes=False)
def is_num(n):
    """Checks if n is a number"""
    if isinstance(n, int):
        return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def is_num_page(n=None):
    """Displays an HTML page if n is an integer"""
    if isinstance(n, int):
        return render_template('5-number_template.html', n=n)


if __name__ == "__main__":
    app.run()
