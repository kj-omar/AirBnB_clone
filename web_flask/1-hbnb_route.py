#!/usr/bin/python3
"""
Script that starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask

# create an instance of the app
# use the option strict_slashes=False
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ This route display 'Hello HBNB' """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Route display “HBNB” """
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
