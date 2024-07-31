#!/usr/bin/python3
"""
This module starts a Flask web application to manage and display information about states.

The application listens on 0.0.0.0, port 5000, and includes the following routes:

    /states: HTML page displaying a list of all State objects.
    /states/<id>: HTML page displaying information about the State with the specified <id>.

Routes:
    /states: Renders a page with a list of all State objects, sorted by name.
    /states/<id>: Renders a page with detailed information about a specific State, if it exists.

The application uses the `storage` object from the `models` module to interact with the data.
The SQLAlchemy session is closed after each request to ensure clean resource management.
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/states", strict_slashes=False)
def states():
    """
    Displays an HTML page with a list of all State objects.

    States are sorted by name and rendered using the '9-states.html' template.
    """
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Displays an HTML page with information about a specific State object.

    The State with the specified <id> is rendered using the '9-states.html' template.
    If the State does not exist, an empty page is rendered.
    """
    states = storage.all("State")
    state = next((s for s in states.values() if s.id == id), None)
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def teardown(exc):
    """
    Closes the SQLAlchemy session after each request.

    This ensures that resources are properly cleaned up.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
