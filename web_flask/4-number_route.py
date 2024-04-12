#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route / display 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route /hbnb display 'HBNB'"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route /c/<text> display 'C ' followed by the text, replace '_' with ' '"""
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Route /python/<text> or /python/ display 'Python ' followed by the text, replace '_' with ' '"""
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"

@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Route /number/<n> display 'n is a number' only if n is an integer"""
    return f"{n} is a number"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
