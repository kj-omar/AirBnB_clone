#!/usr/bin/python3
# Script starts flask application, listening 0.0.0.0:5000.


from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home{}: #view for home
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
