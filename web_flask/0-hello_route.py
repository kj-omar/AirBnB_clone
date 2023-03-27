#!/usr/bin/python3
 """
     starts flask web app
     listens on 0.0.0.0, port 5000
 """
import sys
from flask import Flask


sys.path.append('.')
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function called with / route """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)