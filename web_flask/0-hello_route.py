#!/usr/bin/python3
# Script starts flask application, listening 0.0.0.0:5000.

pip install flask

from flask import Flask

app = Flask(__name__)
@app.route('/')
def home{}: #view for home
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(strict_slashes=False)
