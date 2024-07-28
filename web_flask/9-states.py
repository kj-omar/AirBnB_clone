#!/usr/bin/python3
"""Starts a flask app that uses db storage"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def state_list():
    """Renders 9-states.html in default mode"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode="default")


@app.route("/states/<id>", strict_slashes=False)
def state_list_by_id(id):
    """Renders 9-states.html in id mode"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode="id")
    return render_template('9-states.html', states=state, mode="none")


@app.teardown_appcontext
def teardown(self):
    """Ends current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
