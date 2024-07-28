#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
"this is a python script module"


@app.route("/")
def hello():
    "first flask funciton"
    return "Hello HBNB!$"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
