#!/usr/bin/python3
"""
A simple Flask web application script.

This script initializes a Flask web application with a single route
that responds with "Hello HBNB!" when accessed.

Configuration:
- `app.url_map.strict_slashes` is set to `False` to allow URLs with
  or without a trailing slash to match the same route.

The application runs with the following settings:
- `debug=True` for development auto-reloading and better error messages.
- The server listens on all network interfaces (`0.0.0.0`) on port `5000`.
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
    # Run the Flask application
    # The `debug=True` argument enables debug mode.
    # `host='0.0.0.0'` allows access from any network interface.
    # `port=5000` specifies the port on which the server will listen.
    app.run(debug=True, host='0.0.0.0', port=5000)
