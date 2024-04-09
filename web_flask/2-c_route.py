#!/usr/bin/python3
"""Start a Flask web application"""


from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_main():
    """Display Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB!"""
    return 'HBNB'

@app.route('/c/<text>', script_slashes=False)
def profile(text):
    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
