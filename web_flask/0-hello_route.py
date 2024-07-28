from flask import Flask
app = Flask(__name__)
"this is a python script module"


@app.route("/")
def hello():
    "first flask funciton"
    return "Hello HBNB!$"
