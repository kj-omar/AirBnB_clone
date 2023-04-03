#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    if "_" in text:
        text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/<text>", strict_slashes=False)
def python(text):
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/python", strict_slashes=False)
def python_default():
    return f"Python is cool"


@app.route("/number/<int:n>", strict_slashes=False)
def number_only(n):
    if isinstance(n, int):
        return f"{n} is a number"
    else:
        return


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return f"""<!DOCTYPE html>
                        <HTML lang="en">
                            <HEAD>
                                <TITLE>HBNB</TITLE>
                            </HEAD>
                            <BODY>
                                <H1>Number: {n}</H1>
                            </BODY>
                        </HTML>"""
    else:
        return


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")


