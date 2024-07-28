#!/usr/bin/python3
"""Starts a flask app that uses db storage"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """Renders 7-states_list.html"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """Ends current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
