#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_the_db(exception=None):
    # Function to clear previous session
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    # Function to display html page full of states
    from models.state import State
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
