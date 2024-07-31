#!/usr/bin/python3
"""
A simple Flask web application script.

This script initializes a Flask web application with a single route
that responds with "Hello HBNB!" when accessed.

"""

from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Configure URL handling to be lenient with trailing slashes
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
    Handle requests to the root URL ('/').

    Returns:
        str: A simple greeting message.
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
