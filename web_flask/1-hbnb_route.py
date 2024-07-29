#!/usr/bin/python3
"""Doc Model"""
from flask import Flask


"""Making the App"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Saying Hello to the world"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Saying Hello to the world"""
    return "HBNB"


if __name__  =='__main__':
    app.run(port='5000', host='0.0.0.0')
