#!/usr/bin/python3
"""Doc Model"""
from flask import Flask, render_template
from markupsafe import escape


"""Making the App"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Saying Hello to the world"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def say_hbnb():
    """Saying Hello to the world"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """Saying Hello to the world"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text="is cool"):
    """Saying Hello to the world"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def numbers_only(n):
    """Saying Hello to the world"""
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_page(n):
    """Saying Hello to the world"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def define_odd_even(n):
    """Saying Hello to the world"""
    val = "even"
    if n % 2:
        val = "odd"
    return render_template('6-number_odd_or_even.html', n=n, val=val)


if __name__ =='__main__':
    app.run(port='5000', host='0.0.0.0')