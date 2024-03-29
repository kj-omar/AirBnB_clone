#!/usr/bin/python3
""" A script that starts a Flask web application """
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of State objects in DBStorage.
    States are sorted by name.
    """
    #states = storage.allcd ("State")
    #return render_template("7-states_list.html", states=states)
    states = sorted(storage.all("State").values(), key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
